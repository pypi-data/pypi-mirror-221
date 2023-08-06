from abc import ABC, abstractmethod

import pytorch_lightning as pl
import codefast as cf 

class ModelMetrics(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.pos = 4 if 'pos' not in kwargs else kwargs['pos']

    def __str__(self):
        ignore_keys = ['pos']
        iter_keys = ['epoch']
        class_name = self.__class__.__name__

        def _repr_metric():
            for k, v in self.kwargs.items():
                if k not in ignore_keys:
                    # check if v is a tensor, if so convert to float
                    vv = v.item() if hasattr(v, 'item') else v
                    if k in iter_keys:
                        yield f'{k}={vv}'
                    else:
                        yield f'{k}={round(vv, self.pos)}'

        return f'{class_name}({", ".join([_ for _ in _repr_metric()])})\n'


# Abstract class for callbacks
class ModelMetricsCallback(pl.Callback, ABC):

    def __init__(self):
        self.metrics = []

    @abstractmethod
    def on_validation_epoch_end(self, trainer, pl_module):
        ...

    def on_train_end(self, trainer, pl_module):
        if self.metrics:
            print(self.metrics[-1])


class ModelSaveCallback(pl.Callback):
    """ save best model 
    """

    def __init__(self, save_path: str):
        self.save_path = save_path
        self.best_loss = float('inf')

    def on_validation_epoch_end(self, trainer, pl_module):
        metrics = trainer.callback_metrics
        if 'val_loss' in metrics.keys():
            val_loss = metrics['val_loss'].item()
            if val_loss < self.best_loss:
                self.best_loss = val_loss
                trainer.save_checkpoint(self.save_path)


class PretrainedSaveCallback(pl.Callback):
    """ save best model 
    """

    def __init__(self, save_path: str):
        self.save_path = save_path
        self.best_loss = float('inf')

    def on_validation_epoch_end(self, trainer, pl_module):
        metrics = trainer.callback_metrics
        if 'val_loss' in metrics.keys():
            val_loss = metrics['val_loss'].item()
            if val_loss < self.best_loss:
                self.best_loss = val_loss
                trainer.model.pretrained.save_pretrained(self.save_path)



class AccLossCallback(ModelMetricsCallback):

    def on_validation_epoch_end(self, trainer, pl_module):
        """
        usage: 
        def validation_step(self, batch, batch_idx):
            ...
            metric = {'val_loss': loss, 'val_acc': accuracy}
            self.log_dict(metric)
        """
        metrics = ModelMetrics(
            epoch=trainer.current_epoch,
        )
        import torch 
        for k, v in trainer.callback_metrics.items():
            _v = v.cpu()
            if isinstance(_v, torch.Tensor):
                _v = _v.item()
            metrics.kwargs[k] = _v
        print(metrics)
        self.metrics.append(metrics)
