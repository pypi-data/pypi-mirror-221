import numpy as np
import torch.nn.functional as F
import os
import torch
from torch.utils.data import Dataset
import random 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

class TEPS(Dataset):

  def __init__(self, train: bool, augmentation = None, cuda_device = 0,**kwargs):
    PATH = "/home/cmackinnon/scripts/datasets/TEPS/"
    self.cuda_device = cuda_device
    if train:
      data = np.load(PATH+"train_data.npy")
    else:
      data = np.load(PATH+"test_data.npy")
    data = np.swapaxes(data,1,2)
    if cuda_device == "cpu":
      self.x = torch.from_numpy(data[:,1:,:])
    else:
      self.x = torch.from_numpy(data[:,1:,:]).cuda(cuda_device).float()
    self.y = torch.from_numpy(data[:,0,0])
    if cuda_device == "cpu":
      if kwargs["binary"]:
        self.y = torch.from_numpy(np.where(self.y.numpy() != 0, 1,0)).long()
      else:
        self.y = self.y.long()
    else:
      if kwargs["binary"]:
        self.y = torch.from_numpy(np.where(self.y.numpy() != 0, 1,0)).cuda(cuda_device).long()
      else:
        self.y = self.y.cuda(cuda_device).long()
    self.augmentation = augmentation
  def get_labels(self):
    return self.y
  def disable_augmentation(self):
    self.augmentation = False
  def enable_augmentation(self,aug):
    self.augmentation = aug

  def __getitem__(self, index):
    x, y = self.x[index], self.y[index]
    if self.augmentation:
      for func in self.augmentation:
        x,y = func(x,y)
    return x,y
  
  def get_n_classes(self):
    return len(torch.unique(self.y))
  def get_n_samples(self):
    return self.x.shape[0]
  def get_n_features(self):
    return self.x.shape[1]
  def get_length(self):
    return self.x.shape[2]

  def __len__(self):
    return self.x.shape[0]


class Train_TEPS(TEPS):

  def __init__(self, window_size = 500, augmentation = False,samples_per_class = None,binary = False,one_hot = True,samples_per_epoch = 1,PATH= None,cuda_device = None,sub_set_classes = None): 
    super(Train_TEPS,self).__init__(True, augmentation,samples_per_class = samples_per_class,binary = binary ,one_hot = one_hot,samples_per_epoch = samples_per_epoch,PATH = PATH,cuda_device = cuda_device,sub_set_classes = sub_set_classes)

class Test_TEPS(TEPS):

  def __init__(self, window_size = 500, augmentation = False,samples_per_class = None,binary = False,one_hot = False,samples_per_epoch = 1,cuda_device = None,sub_set_classes = None): 
    super(Test_TEPS,self).__init__(False , augmentation,samples_per_class =samples_per_class,binary = binary ,one_hot = one_hot,samples_per_epoch = samples_per_epoch,cuda_device = cuda_device,sub_set_classes = sub_set_classes)

