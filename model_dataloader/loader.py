import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import Dataset


class GraphDataset(Dataset):
    def __init__(self, path_list, batch_size):
        self.path_list  = path_list
        self.batch_size = batch_size

    # def __one_hot_vector__(self):
    #     test = np.zeros(shape = 3)
    #     test[self.label-1] = 1
    #     return test
        
    def __len__(self):
        return len(self.path_list)
    
    def __getitem__(self, index):
        batch_data = self.path_list[index]
        self.graph = np.array(batch_data[0])
        self.label = np.array(batch_data[1])

        self.I     = np.matrix(np.eye(self.graph.shape[0]))

        graph = self.graph + self.I
        label = self.label - 1

        graph = torch.from_numpy(graph)
        label = torch.from_numpy(np.asarray(label))
        graph = graph.float()
        label = label.long()
        return graph, label