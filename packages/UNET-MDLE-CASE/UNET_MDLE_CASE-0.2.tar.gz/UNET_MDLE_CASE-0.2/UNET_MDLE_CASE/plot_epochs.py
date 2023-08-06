import numpy as np
from skimage.io import imread,imshow
from skimage.transform import resize
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import random
import numpy as np
import subprocess
import sys
import string
import os.path
import re
import matplotlib.pyplot as plt
import pandas as pd
import math


def plot_epochs(csvfile):
    """
    Generates plots of loss and accuracy for training and validation 
    
    Authors:
        Zhuldyz Ualikhankyzy, Tommy Ciardi 

    :param csvfile: a csv file with the metrics for each epoch 
    :type csvfile: string 
       
    """

    df = pd.read_csv(csvfile)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(df['loss'])
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('loss')
    axes[0].set_title('Training Loss')

    axes[1].plot(df['val_loss'])
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('loss')
    axes[1].set_title('Validation Loss')
    plt.tight_layout()
    plt.show()

    plt.close()

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(df['accuracy'])
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('accuracy')
    axes[0].set_title('Training Accuracy')

    axes[1].plot(df['val_accuracy'])
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('accuracy')
    axes[1].set_title('Validation Accuracy')
    plt.tight_layout()
    plt.show()