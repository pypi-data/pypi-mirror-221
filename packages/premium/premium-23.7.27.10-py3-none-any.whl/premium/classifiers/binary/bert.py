#!/usr/bin/env python3

from functools import cached_property
from typing import Dict

import pandas as pd
import pytorch_lightning as pl
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, Dataset, random_split
from transformers import BertModel, BertTokenizer

from premium.classifiers.binary.bases import NNModel, calculate_metrics
from premium.lightning.callbacks import AccLossCallback

MODEL = 'bert-base-uncased'


class CustomDataset(Dataset):

    def __init__(self,
                 df: pd.DataFrame,
                 tokenizer: BertTokenizer,
                 max_len: int = 200):
        self.texts = df['text'].tolist()
        self.labels = df['label'].tolist()
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoded = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt',
        )
        input_ids = encoded['input_ids']
        attention_mask = encoded['attention_mask']
        return {
            'input_ids': input_ids.flatten(),
            'attention_mask': attention_mask.flatten(),
            'label': torch.tensor(label),
        }


class BertClassifier(nn.Module):

    def __init__(self, freeze_bert=False, model_name=MODEL):
        super(BertClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(model_name)
        self.dropout = nn.Dropout(0.3)
        self.linear = nn.Linear(768, 1)
        self.sigmoid = nn.Sigmoid()
        if freeze_bert:
            for param in self.bert.parameters():
                param.requires_grad = False

    def forward(self, input_ids, attention_mask):
        output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = output.pooler_output
        pooled_output = self.dropout(pooled_output)
        linear_output = self.linear(pooled_output)
        proba = self.sigmoid(linear_output).squeeze(1)
        return proba


class DataModule(pl.LightningDataModule):

    def __init__(self, csv_file, batch_size=64, max_len=200):
        super().__init__()
        self.batch_size = batch_size
        self.max_len = max_len
        self.df = pd.read_csv(csv_file)

    def prepare_data(self):
        pass

    def setup(self, stage=None):
        tokenizer = BertTokenizer.from_pretrained(MODEL)
        dataset = CustomDataset(self.df, tokenizer, self.max_len)
        train_size = int(0.8 * len(dataset))
        val_size = int(0.1 * len(dataset))
        test_size = len(dataset) - train_size - val_size
        self.train_dataset, self.val_dataset, self.test_dataset = random_split(
            dataset, [train_size, val_size, test_size])

    def train_dataloader(self):
        return DataLoader(self.train_dataset,
                          batch_size=self.batch_size,
                          num_workers=4,
                          pin_memory=True,
                          shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset,
                          batch_size=self.batch_size,
                          pin_memory=True,
                          num_workers=4)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size)


class Classifier(pl.LightningModule):

    def __init__(self, num_classes=1, model_name=MODEL):
        super().__init__()
        self.save_hyperparameters()
        self.criterion = nn.BCELoss()
        self.model = BertClassifier(False, model_name)

    def forward(self, input_ids, attention_mask):
        return self.model(input_ids, attention_mask)

    def training_step(self, batch, batch_idx):
        input_ids, attention_mask, labels = batch['input_ids'], batch[
            'attention_mask'], batch['label']
        outputs = self.model(input_ids, attention_mask)
        loss = self.criterion(outputs, labels.float())
        self.log('train_loss', loss)
        return loss

    def validation_step(self, batch, batch_idx):
        input_ids, attention_mask, labels = batch['input_ids'], batch[
            'attention_mask'], batch['label']
        outputs = self.model(input_ids, attention_mask)
        loss = self.criterion(outputs, labels.float())
        preds = (outputs > 0.5).int()
        acc = accuracy_score(labels.cpu(), preds.cpu())
        metrics = {'val_acc': acc, 'val_loss': loss}
        self.log_dict(metrics)
        return metrics

    def test_step(self, batch, batch_idx):
        input_ids, attention_mask, labels = batch['input_ids'], batch[
            'attention_mask'], batch['label']
        outputs = self.model(input_ids, attention_mask)
        loss = self.criterion(outputs, labels.float())
        preds = (outputs > 0.5).int()
        metrics = calculate_metrics(labels.cpu(), preds.cpu())
        results = {**{'test_loss': loss}, **metrics}
        self.log_dict(results)
        return results

    def configure_optimizers(self):
        return torch.optim.AdamW(self.parameters(), lr=2e-5)


class BertBinary(NNModel):
    """ For benchmarking binary classification with BERT
    """

    def __init__(self, epochs=2, batch_size=64, max_len=200, model_name=MODEL):
        super().__init__()
        self.name += ':bert'
        self.epochs = epochs
        self.batch_size = batch_size
        self.max_len = max_len
        self._model_name = model_name

    @cached_property
    def bert_model(self):
        return Classifier(self._model_name)

    @cached_property
    def tokenizer(self):
        return BertTokenizer.from_pretrained(self._model_name)

    @cached_property
    def trainer(self):
        callbacks = [AccLossCallback()]
        device = 'gpu' if torch.cuda.is_available() else 'cpu'
        return pl.Trainer(accelerator=device,
                          max_epochs=self.epochs,
                          callbacks=callbacks)

    def get_data_loader(self, df):
        ds = CustomDataset(df, self.tokenizer, self.max_len)
        return DataLoader(ds,
                          batch_size=self.batch_size,
                          num_workers=4,
                          pin_memory=True,
                          shuffle=True)

    def fit(self, X):
        Xt, Xv = train_test_split(X, test_size=0.2, random_state=42)
        self.train_loader = self.get_data_loader(Xt)
        self.val_loader = self.get_data_loader(Xv)
        self.trainer.fit(self.bert_model, self.train_loader, self.val_loader)

    def evaluate(self, Xt: pd.DataFrame) -> Dict:
        test_loader = self.get_data_loader(Xt)
        return self.trainer.test(dataloaders=test_loader)[0]

    def run(self, X, Xt):
        return self.inner_run(X, Xt)


if __name__ == '__main__':
    bb = BertBinary(epochs=1, batch_size=16, max_len=200)
    df = pd.read_csv('/tmp/headimdb.csv')
    X, Xt = train_test_split(df, test_size=0.2, random_state=42)
    x = bb.run(X, Xt)
    print(x)
