import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sn 
import warnings
from tqdm.notebook import tqdm
warnings.filterwarnings('ignore')
#%matplotlib inline
from keras.preprocessing.image import load_img
from keras.models import Sequential,Model
from keras.layers import Dense,Conv2D,Dropout,Flatten,MaxPooling2D,Input

#dataset=r"C:\Users\hp\Downloads\utkcropped"
import os

DATASET_PATH = r"C:\Users\hp\Downloads\utkcropped"

print("Folder exists:", os.path.exists(DATASET_PATH))
print("Total files:", len(os.listdir(DATASET_PATH)))
print("First 5 files:", os.listdir(DATASET_PATH)[:5])


