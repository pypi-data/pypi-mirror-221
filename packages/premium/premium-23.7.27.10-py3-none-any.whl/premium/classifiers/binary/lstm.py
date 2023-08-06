#!/usr/bin/env python3
import pandas as pd
import pytorch_lightning as pl
import torch
import torch.nn as nn
from pydantic import BaseModel
from sklearn.metrics import accuracy_score

from premium.classifiers.binary.bases import NNModel, calculate_metrics
from premium.classifiers.binary.dataset import TextDataModule
from premium.lightning.callbacks import AccLossCallback, ModelSaveCallback
from premium.pytorch.data import TextDataset

torch.manual_seed(1)
_DEVICE = 'CUDA' if torch.cuda.is_available() else 'cpu'


class _LSTM(nn.Module):
    '''
    '''

    def __init__(self, embedding_dim, hidden_dim, vocab_size, output_size,
                 batch_size):
        '''
        embedding_dim: Glove is 300. We are using 6 here.
        hidden_dim: can be anything, usually 32 or 64. We are using 6 here.
        vocab_size: vocabulary size includes an index for padding.
        output_size: We need to exclude the index for padding here.
        '''
        super().__init__()
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        self.word_embeddings = nn.Embedding(vocab_size,
                                            embedding_dim,
                                            padding_idx=0)
        self.batch_size = batch_size
        self.num_layers = 2
        self.num_directions = 2
        self.lstm = nn.LSTM(embedding_dim,
                            hidden_dim,
                            batch_first=True,
                            num_layers=self.num_layers,
                            bidirectional=(self.num_directions == 2))
        self.fc1 = nn.Linear(2 * hidden_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_size)
        self.dropout = nn.Dropout(0.3)

    def init_hidden(self):
        '''
        Initiate hidden states.
        '''
        # Shape for hidden state and cell state:
        # num_layers * num_directions, batch, hidden_size
        # i.e., (1, 32, 64) if bidirectional=False else (2, 32, 64)
        dim1 = self.num_layers * self.num_directions
        h_0 = torch.randn(dim1, self.batch_size, self.hidden_dim)
        c_0 = torch.randn(dim1, self.batch_size, self.hidden_dim)

        # The Variable API is now semi-deprecated, so we use nn.Parameter instead.
        # Note: For Variable API requires_grad=False by default;
        # For Parameter API requires_grad=True by default.
        h_0 = nn.Parameter(h_0, requires_grad=True)
        c_0 = nn.Parameter(c_0, requires_grad=True)

        return (h_0, c_0)

    def forward(self, sentences, X_lengths):
        '''
        Parameters
        ----------
        sentences: padded sentences tensor. Each element of the tensor is an array of words.
        X_lengths: length of sentence tensor. Each element of the tensor is the original
        length of the unpadded sentence.

        Returns
        -------
        '''
        hidden_0 = self.init_hidden()
        batch_size, seq_len = sentences.size()
        embeds = self.word_embeddings(sentences)

        embeds = torch.nn.utils.rnn.pack_padded_sequence(embeds,
                                                         X_lengths.cpu(),
                                                         batch_first=True,
                                                         enforce_sorted=False)
        if _DEVICE == 'CUDA':
            embeds = embeds.to(torch.device('cuda'))
            hidden_0 = (hidden_0[0].to(torch.device('cuda')),
                        hidden_0[1].to(torch.device('cuda')))

        lstm_out, (hidden, cell) = self.lstm(embeds, hidden_0)
        # Note: parsing in total_length is a must, otherwise you might run into dimension mismatch.
        lstm_out, _ = torch.nn.utils.rnn.pad_packed_sequence(lstm_out,
                                                             batch_first=True)
        lstm_out_forward = lstm_out[torch.arange(batch_size),
                                    X_lengths - 1, :self.hidden_dim]
        lstm_out_reverse = lstm_out[:, 0, self.hidden_dim:]
        # tag_scores = self.f1(torch.cat((lstm_out_forward, lstm_out_reverse), dim=1))
        hidden = self.dropout(
            torch.cat((lstm_out_forward, lstm_out_reverse), dim=1))
        output = self.fc1(hidden)
        output = self.dropout(output)
        tag_scores = self.fc2(output)
        tag_scores_flat = torch.squeeze(tag_scores, 1)
        return torch.sigmoid(tag_scores_flat)


def accuracy(y, y_hat):
    """ device agnostic accuracy calculation
    """
    y = y.cpu().numpy()
    y_hat = y_hat.cpu().numpy()
    return accuracy_score(y, y_hat.round())


def to_cpu(x):
    if x.device.type == "cuda":
        return x.cpu()
    return x


class LightningModel(pl.LightningModule):
    """ Pytorch Lightning LSTM Classifier
    """

    def __init__(self, embedding_dim: int, hidden_dim: int, vocab_size: int,
                 num_classes: int, batch_size: int, train_loader, val_loader
                 ):
        super().__init__()
        self.model = _LSTM(embedding_dim, hidden_dim, vocab_size, num_classes,
                           batch_size)
        self.criterion = nn.BCELoss()
        self.train_loader = train_loader
        self.val_loader = val_loader

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y, x_len = batch
        y_hat = self.model(x, x_len)
        loss = self.criterion(y_hat.float(), y.float())
        self.log('train_loss', loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y, x_len = batch
        y_hat = self.model(x, x_len)
        loss = self.criterion(y_hat.float(), y.float())
        acc = accuracy(y, y_hat)
        self.log_dict({'val_loss': loss, 'val_acc': acc})
        return loss

    def test_step(self, batch, batch_idx):
        x, y, x_len = batch
        y_hat = self.model(x, x_len)
        loss = self.criterion(y_hat.float(), y.float())
        metrics = calculate_metrics(to_cpu(y), to_cpu(y_hat).round())
        result = {'test_loss': loss, **metrics}
        self.log_dict(result)
        return result

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)

    def train_dataloader(self):
        return self.train_loader

    def val_dataloader(self):
        return self.val_loader


class LSTMInput(BaseModel):
    embedding_dim: int
    hidden_dim: int
    seq_len: int
    epochs: int = 10
    batch_size: int = 32


class LSTMBinaryClassifier(NNModel):

    def __init__(self, rinput: LSTMInput):
        super().__init__()
        self.embedding_dim = rinput.embedding_dim
        self.hidden_dim = rinput.hidden_dim
        self.seq_len = rinput.seq_len
        self.epochs = rinput.epochs
        self.batch_size = rinput.batch_size
        self.d_module = None

    @property
    def callbacks(self):
        from pytorch_lightning.callbacks.early_stopping import EarlyStopping
        return [AccLossCallback(),
                EarlyStopping(monitor='val_loss',
                              mode='min',
                              min_delta=0.01,
                              patience=3)]

    def fit(self, X: pd.DataFrame):
        """ X is a dataframe with columns 'text' and 'label'
        """
        self.d_module = TextDataModule(TextDataset(df=X), self.batch_size,
                                       self.seq_len)
        self.d_module.setup(stage='fit')
        Xt, Xv = self.d_module.train_dataloader(
        ), self.d_module.val_dataloader()
        vocab_size = self.d_module.vocab_size
        self.trainer = pl.Trainer(max_epochs=self.epochs,
                                  callbacks=self.callbacks,
                                  accelerator='gpu' if _DEVICE == 'CUDA' else 'cpu')
        self.clf = LightningModel(embedding_dim=self.embedding_dim,
                                  hidden_dim=self.hidden_dim,
                                  vocab_size=vocab_size,
                                  num_classes=1,
                                  batch_size=self.batch_size,
                                  train_loader=Xt,
                                  val_loader=Xv
                                  )
        self.trainer.fit(self.clf)

    def evaluate(self, Xe: pd.DataFrame) -> float:
        self.d_module.reset_data(TextDataset(df=Xe))
        self.d_module.setup(stage='test')
        Xe = self.d_module.test_dataloader()
        result = self.trainer.test(self.clf, Xe)[0]
        return result

    def run(self, X, Xt):
        self.name += ':lstm'
        return self.inner_run(X, Xt)
