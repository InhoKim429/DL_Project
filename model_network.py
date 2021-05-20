import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self, hidden_dim = [492, 512, 256, 128, 64, 3]):
        super(Net, self).__init__()
        self.hidden_dim = hidden_dim
        self.gelu    = nn.GELU()
        self.softmax = nn.Softmax(dim = 1)

        self.linear1 = nn.Linear(492, self.hidden_dim[0])
        self.linear2 = nn.Linear(self.hidden_dim[0], self.hidden_dim[1])
        self.linear3 = nn.Linear(self.hidden_dim[1], self.hidden_dim[2])
        self.linear4 = nn.Linear(self.hidden_dim[2], self.hidden_dim[3])
        self.linear5 = nn.Linear(self.hidden_dim[3], self.hidden_dim[4])
        self.linear6 = nn.Linear(self.hidden_dim[4], self.hidden_dim[5])
        # self.linear7 = nn.Linear(self.hidden_dim[4], self.hidden_dim[5])
        self.sequential = nn.Sequential(
                                self.linear1,
                                self.gelu,
                                self.linear2,
                                self.gelu,
                                self.linear3,
                                self.gelu,
                                self.linear4,
                                self.gelu,
                                self.linear5,
                                self.gelu,
                                self.linear6)

        self.last_linear = nn.Linear(9, 3)
    def forward(self, graph):
        out = self.sequential(graph)
        out = out.permute(0, 2, 1)
        out = self.sequential(out)

        B, H, W = out.shape
        out = out.view(B, -1)
        out = self.last_linear(out)
        out = self.softmax(out)
        return out