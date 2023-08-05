import numpy as np
import torch
from torch.utils.data import Dataset
import random 
from sklearn.preprocessing import StandardScaler
from HPO.utils.time_series_augmentation import permutation , magnitude_warp, time_warp, window_slice, jitter, scaling, rotation
import os
def none(x):
  return x
class TEPS(Dataset):
  def __init__(self, window_size, x : str , y : str ):
    path = "datasets/TEPS/"
    self.x = torch.from_numpy(np.reshape(np.load(path+x),(-1,52)))
    self.y = torch.from_numpy(np.load(path+y))
    
    self.n_samples = self.x.shape[0]
    self.window = window_size
    self.n_classes = len(np.unique(self.y))

  def set_window_size(self, window_size):
    self.window = window_size
  def __getitem__(self, index):
    while index+self.window > self.n_samples:
      index = random.randint(0,self.n_samples)
    x = self.x[index:index+self.window]
    y = self.y[index+self.window-1]
    x = x.reshape(52,self.window)
    return x, y
  
  def get_n_classes(self):
    return self.n_classes
  def get_n_samples(self):
    return self.n_samples

  def __len__(self):
    return self.n_samples - self.n_samples%self.window


class Train_TEPS(TEPS):

  def __init__(self, window_size = 200): 
    super().__init__(window_size, "x_train.npy","y_train.npy")

class Test_TEPS(TEPS):
  def __init__(self, window_size = 200): 
    super().__init__(window_size, "x_test.npy","y_test.npy")

class BTC(Dataset):
  def __init__(self, window_size, prediction_distance, split):
    self.path ="{}/scripts/datasets/BTC/BTC.npy".format(os.environ["HOME"])
    self.prediction_distance = prediction_distance
    self.x = torch.from_numpy(np.reshape(np.load(self.path),(-1,10)))[1000000:,:]
    if split > 0.5:
      self.x = self.x[:int(self.x.shape[0]*split)]
    else:
      self.x = self.x[-int(self.x.shape[0]*split):]
    self.n_samples = self.x.shape[0]
    ss = StandardScaler()
    self.x = ss.fit_transform(self.x)
    self.window = window_size
    self.generate_percent_labels()
    self.n_features = self.x.shape[1]
    self.n_classes = len(np.unique(self.y))
    print(self.y)
    for i in range(self.n_classes):
      print(np.count_nonzero(self.y == i))

    print(len(np.unique(self.y)))
  def generate_labels(self):
    idx = 3
    self.y = []
    for i in range(self.n_samples- self.prediction_distance):
        if self.x[i+self.prediction_distance,idx] > self.x[i,idx]:
          self.y.append(1)
        else:
          self.y.append(0)
    print(self.x.shape[0])


  def generate_percent_labels(self, classes = [0.01,0.1,0.25,0.5,0.75,0.9,0.99,1]):
    abs_change = np.diff(self.x[:,3])
    self.class_labels = {}
    per_change = np.divide(abs_change , self.x[1:,3])
    i_last = 0 
    self.y = np.zeros(self.x.shape[0])
    for c,i in enumerate(classes):
      self.class_labels[c] = "{}-{}".format(i_last,i)
      print(np.nanquantile(per_change, i))
      hold = np.where( (per_change > np.nanquantile(per_change,i_last)) & (per_change < np.nanquantile(per_change,i)))
      i_last = i 
      self.y[hold] = c
    
    print(len(self.y))
    print(self.x.shape[0])



  def set_window_size(self, window_size):
    self.window = window_size
  def __getitem__(self, index):
    while index+self.window+self.prediction_distance > self.n_samples:
      index = random.randint(0,self.n_samples)
    x = self.x[index:index+self.window]
    y = self.y[index+self.window-1]
    x = x.reshape(10,self.window)
    return x, y
  
  def get_n_classes(self):
    return self.n_classes
  def get_n_samples(self):
    return self.n_samples
  def get_n_features(self):
    return self.n_features

  def __len__(self):
    return self.n_samples - self.n_samples%self.window


class Train_BTC(BTC):

  def __init__(self, window_size = 100, split = 0.95 , pred_dist = 1 ): 
    super().__init__(window_size, split = split, prediction_distance = pred_dist)

class Test_BTC(BTC):
  def __init__(self, window_size = 100, split = 0.05, pred_dist = 1): 
    super().__init__(window_size,split = split, prediction_distance = pred_dist)



class repsol(Dataset):
  def __init__(self, window_size, files : list , augmentations):
    path = "/home/snaags/scripts/datasets/"
    data = []
    self.x_index_address = {}
    self.y_index_address = {}
    self.window = window_size
    augmentations_per_batch = 2
    #index_list sum()
    if augmentations == True:
      self.non_warp_augmentations =[jitter, scaling, rotation, permutation ]
      self.warp_augmentations = [magnitude_warp, time_warp]
    for i in files:
      data.append(np.reshape(np.load(path+i),(-1,28)))
    self.current_index = 0
    use_all = True

  
    for batch in data:
      batch_x = batch[:,1:]
      batch_y = batch[:,0]
      self.add_to_dataset(batch_x,batch_y)
      if augmentations:
        if use_all == True:
          x = batch_x.reshape(1,batch_x.shape[0],batch_x.shape[1])
          augs = self.warp_augmentations +self.non_warp_augmentations
          for i in range(len(augs)):
              x = augs.pop(random.randint(0,len(augs) -1))(x)
          self.add_to_dataset(x.reshape(*x.shape[1:]),batch_y)
        else:
          for i in range(augmentations_per_batch):
            augmentations_for_current_batch = []
            temp_augmentation_list = self.non_warp_augmentations.copy()
            augmentations_for_current_batch.append(random.choice(self.warp_augmentations))
            x = batch_x.reshape(1,batch_x.shape[0],batch_x.shape[1])
            while len(augmentations_for_current_batch) < 3:
              augmentations_for_current_batch.append(temp_augmentation_list.pop(random.randint(0,len(temp_augmentation_list)-1)))
      
            for augmentation_function in augmentations_for_current_batch:
              x = augmentation_function(x)
            self.add_to_dataset(x.reshape(*x.shape[1:]),batch_y)

    
    self.n_samples = self.current_index #* len(self.augmentations)
    self.features = 27
    self.n_classes = 2
  def add_to_dataset(self,x,y):
    self.x_index_address[self.current_index] = torch.from_numpy(x)
    self.y_index_address[self.current_index] = torch.from_numpy(y)
    self.current_index += x.shape[0] - self.window

  def set_window_size(self, window_size):
    self.window = window_size

  def __getitem__(self, index):
    #index_address keys are the first usable index in a batch for the window size
    #this means the index
    addr = 0
    augmentation_idx = 0
    #while index > self.real_samples:
    #  index -= self.real_samples
    #  augmentation_idx += 1 


    for i in self.x_index_address:
      if (index - i) < 0:
        break
      else:
        addr = i

    index -= addr 
    x = self.x_index_address[addr]
    y = self.y_index_address[addr]

    x = x[index:index+self.window]
    y = y[index+self.window-1]

    return x.reshape( 27,self.window ) , y
  
  def get_n_classes(self):
    return self.n_classes
  def get_n_samples(self):
    return self.n_samples

  def __len__(self):
    return self.n_samples - self.n_samples%self.window


class Train_repsol(repsol):

  def __init__(self, train_files, window_size = 200, augmentations = True): 
    super().__init__(window_size, train_files, augmentations)

class Test_repsol(repsol):

  def __init__(self,test_files, window_size = 200, augmentations = False): 
    super().__init__(window_size, test_files , augmentations)


class TEPS_split(Dataset):
  def __init__(self, window_size, train , augmentations, max_samples):


    self.features = 52
    self.n_classes = 21
    self.samples_per_class = [0]* self.n_classes
    self.max_samples = max_samples

    path = "/home/snaags/scripts/datasets/TEPS/split/"
    files = os.listdir(path)
    if train == True:
      filtr = "training"
    else:
      filtr = "testing"
    files = [ name for name in files if filtr in name]    
    
    num_files = max_samples / 500 
    while len(files) > num_files:
      files.pop(random.randint(0, len(files)-1))
     
    data = []
    self.x_index_address = {}
    self.y_index_address = {}
    self.window = window_size
    while len(files):
      data.append(np.reshape(np.load(path+files.pop(random.randint(0, len(files)-1))),(-1,53)))
    self.current_index = 0
    use_all = True
  
    for batch in data:
      batch_x = batch[:,1:]
      batch_y = batch[:,0]
      self.add_to_dataset(batch_x,batch_y)

    self.n_samples = self.current_index #* len(self.augmentations)
 
  def add_to_dataset(self,x,y):
    self.x_index_address[self.current_index] = torch.from_numpy(x.reshape(52,-1)).float()
    self.y_index_address[self.current_index] = torch.from_numpy(np.unique(y)).long()
    self.samples_per_class[int(y[0])] += x.shape[0]
    self.current_index += 1

  def get_n_samples_per_class(self):
    for i in range(self.n_classes):
      print("Samples in class {}: {}".format(i, self.samples_per_class[i]))    

  def set_window_size(self, window_size):
    self.window = window_size

  def __getitem__(self, index):
    #index_address keys are the first usable index in a batch for the window size
    #this means the index

    
    x = self.x_index_address[index]
    y = self.y_index_address[index]


    return x , y
  
  def get_n_classes(self):
    return self.n_classes
  def get_n_samples(self):
    return self.n_samples
  def get_n_features(self):
    return self.n_samples

  def __len__(self):
    return self.n_samples -1  


class Train_TEPS_split(TEPS_split):

  def __init__(self, window_size = 500, augmentations = False, max_samples = 8000000): 
    super().__init__(window_size, True, augmentations,max_samples)

class Test_TEPS_split(TEPS_split):

  def __init__(self, window_size = 500, augmentations = False, max_samples = 4800000): 
    super().__init__(window_size,  False , augmentations,max_samples)


class TEPS_split_binary(Dataset):
  def __init__(self, window_size, files : list , augmentations, max_samples):


    self.features = 52
    self.n_classes = 2
    self.samples_per_class = [0]* self.n_classes
    self.max_samples = max_samples

    path = "/home/snaags/scripts/datasets/TEPS/split/"
    data = []
    self.x_index_address = {}
    self.y_index_address = {}
    self.window = window_size
    while len(files) and min(self.samples_per_class) < max_samples:
      data.append(np.reshape(np.load(path+files.pop(random.randint(0, len(files)-1))),(-1,53)))
    self.current_index = 0
    use_all = True
  
    for batch in data:
      batch_x = batch[:,1:]
      batch_y = batch[:,0]
      self.add_to_dataset(batch_x,batch_y)

    self.n_samples = self.current_index #* len(self.augmentations)
 
  def add_to_dataset(self,x,y):
    y = np.where(y > 0, 1, 0) #Binarize Classes
    if self.samples_per_class[1]  < self.max_samples or np.unique(y)[0] == 0:
      self.x_index_address[self.current_index] = torch.from_numpy(x)
      self.y_index_address[self.current_index] = torch.from_numpy(y)
   
      if y[0] == 0:
        self.samples_per_class[0] += x.shape[0]
      else:
        self.samples_per_class[1] += x.shape[0]
      self.current_index += x.shape[0] - self.window

  def get_n_samples_per_class(self):
    for i in range(self.n_classes):
      print("Samples in class {}: {}".format(i, self.samples_per_class[i]))    

  def set_window_size(self, window_size):
    self.window = window_size

  def __getitem__(self, index):
    #index_address keys are the first usable index in a batch for the window size
    #this means the index

    for i in self.x_index_address:
      if (index - i) < 0:
        break
      else:
        addr = i

    index -= addr 
    x = self.x_index_address[addr]
    y = self.y_index_address[addr]

    x = x[index:index+self.window]
    y = y[index+self.window-1]

    return x.reshape( 52,self.window ) , y
  
  def get_n_classes(self):
    return self.n_classes
  def get_n_samples(self):
    return self.n_samples

  def __len__(self):
    return self.n_samples - self.n_samples%self.window


class Train_TEPS_split_binary(TEPS_split_binary):

  def __init__(self, train_files, window_size = 200, augmentations = True, max_samples = 250000): 
    super().__init__(window_size, train_files, augmentations,max_samples)

class Test_TEPS_split_binary(TEPS_split_binary):

  def __init__(self,test_files, window_size = 200, augmentations = False, max_samples = 480000): 
    super().__init__(window_size, test_files , augmentations,max_samples)


class Subset(Dataset):
    """
    Subset of a dataset at specified indices.
    Arguments:
        dataset (Dataset): The whole Dataset
        indices (sequence): Indices in the whole set selected for subset
    """
    def __init__(self, dataset, indices):
        self.dataset = dataset
        self.indices = indices

    def __len__(self):
        if self.indices.shape == ():
            return 1
        else:
            return len(self.indices)
    def get_n_classes(self):
      return self.dataset.get_n_classes()
    def get_n_features(self):
      return self.dataset.get_n_features()
    def __getitem__(self, idx):
        return self.dataset[self.indices[idx]]
