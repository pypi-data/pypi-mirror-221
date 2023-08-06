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
import cv2
from PIL import Image
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model

from  .plot_epochs import plot_epochs 
from .pullcsv import pullcsv
 


def train(X_train,Y_train,X_test,Y_test,model, validation_split, batch_size, epochs, patience=100, monitor='val_loss', best=False):
    """
    Trains the model with given architecture, X and Y data, as well as other parameters

    Authors:
        Zhuldyz Ualikhankyzy, Tommy Ciardi 

    :param X_train: X train images 
    :type X_train: list of numpy.ndarray 
    :param Y_train: Y train images
    :type Y_train: list of numpy.ndarray  
    :param X_test: X test images 
    :type X_test: list of numpy.ndarray 
    :param Y_test: Y test images
    :type Y_test: list of numpy.ndarray 
    :param model: model to be used   
    :type model: TensorFlow Keras Model  
    :param validation_split: the fraction of the dataset to be used in validation 
    :type validation_split: float  
    :param batch_size: number of data samples that will be processed together in each forward and backward pass during training  
    :type batch_size: integer 
    :param epochs: number of times the entire dataset will be passed through the model during training
    :type epochs: integer  
    :param patience: number of epochs to wait before stopping the training process if early stopping is on 
    :type patience: integer  
    :param monitor: metric that the early stopping algorithm should monitor to determine whether to stop the training process or not  
    :type monitor: string  
    :param best: if true, then the best model is saved, otherwise, the last iteration is saved 
    :type best: boolean  
    :return filename: name of the intial txt file
    :rtype filename: string
    :return modelweights: name of the file with the weights of the trained model 
    :rtype modelweights: string
    """

    callbacks = [tf.keras.callbacks.EarlyStopping(patience=patience, monitor=monitor)]

    while True:
        filename = 'output' + ''.join(random.choices(string.digits, k=5)) + '.txt'
        if not os.path.exists(filename):
            break

    modelweights = re.findall(r'\d+', filename)[0] + '_weights.h5'
    
    if best:
        # Create a callback to save the best model weights
        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=modelweights,
            monitor=monitor,
            save_best_only=True,
            mode='auto',
            verbose=1
        )
        callbacks.append(checkpoint_callback)

    sys.stdout = open(filename, 'w')
    results = model.fit(X_train, Y_train, validation_split=validation_split, batch_size= batch_size, epochs=epochs, callbacks=callbacks)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    
    model.save_weights(modelweights)
    csvfile = pullcsv(filename)
    plot_epochs(csvfile)
    return filename,modelweights