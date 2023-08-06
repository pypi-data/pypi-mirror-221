import numpy as np
import pytorch_lightning as pl
import torch


class LightningBase(pl.LightningModule):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_epoch_start(self):
        print(
            f'progress: epoch {self.current_epoch+1}/{self.trainer.max_epochs}')

    def validation_epoch_end(self, outputs):
        avg_f1 = np.array([x["val_f1"] for x in outputs]).mean()
        self.log("avg_val_f1", avg_f1, prog_bar=True)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=5e-5)
