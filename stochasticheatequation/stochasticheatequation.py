import numpy as np
import torch
import os
from torch.utils.data import TensorDataset
import scipy.sparse



class StochasticHeatEquation():
    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.data_directory = os.path.join(os.path.dirname(__file__), 'data')
        self.t=torch.tensor(np.load(os.path.join(self.data_directory, 't.npy')),dtype=torch.float32)
        self.x=torch.tensor(np.load(os.path.join(self.data_directory, 'x.npy')),dtype=torch.float32)
        self.u=torch.tensor(np.load(os.path.join(self.data_directory, 'ut.npy')),dtype=torch.float32).unsqueeze(-1)
        self.train_dataset=TensorDataset(self.u)
        self.train_loader=torch.utils.data.DataLoader(self.train_dataset,batch_size=batch_size,shuffle=False)


