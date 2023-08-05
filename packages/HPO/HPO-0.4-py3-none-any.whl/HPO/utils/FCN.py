import torch.nn as nn
import torch

class layer(nn.Module):
  def __init__(self, idx , channels , kernels):
    super(layer, self).__init__()
    self.conv = nn.Conv1d(channels[idx],channels [idx + 1], kernels[idx])
    self.bn = nn.BatchNorm1d(channels[idx+1])
    self.act = nn.ReLU()

  def forward(self , x):
    out = self.conv(x)
    out = self.bn(out)
    return self.act(out)


class FCN(nn.Module):
  def __init__(self, input_size , channels = [64 , 64, 64] , kernels = [8 , 5, 3]  , classes = 2):
    super(FCN,self).__init__()
    self.channels = channels
    self.stem = nn.Conv1d(input_size , channels[0], 1 )
    self.layers = nn.ModuleList()
    self.GAP = nn.AdaptiveAvgPool1d(1)
    self.fc = nn.Linear(channels[-1], classes)
    self.act = nn.ReLU()
    self.fcact = nn.Softmax()
    for idx in range(len(channels[:-1])):
        self.layers.append(layer(idx , channels , kernels))
 
  def get_channels(self):
    return self.channels[-1]

  def _forward(self , x ):
    x = self.stem(x)
    for i in self.layers:
      x = i.forward(x)
    x = self.GAP(x)
    return torch.flatten(x, 1)
  
  def forward(self, x):
    x = self._forward(x)
    return self.fcact(self.fc(x))
