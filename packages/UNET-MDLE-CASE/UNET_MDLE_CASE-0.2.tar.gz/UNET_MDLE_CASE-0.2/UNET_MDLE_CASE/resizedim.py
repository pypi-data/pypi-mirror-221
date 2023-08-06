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

def resizedim(X_train_paths,dim):
    """
    If dimension is not given (means it is (0,0) by defualt) then takes the shape of the first image in X_train as dimension for the all training and testing data 
    Ensures that the images are in square format or square format is requested 
    If dimesion is given, then it sets that dimension for the all training and testing data after after ensuring that the dimesion is valid
    for U-Net, otherwise it takes the closest permissible value to the input value

    Authors:
        Zhuldyz Ualikhankyzy, Tommy Ciardi 

    :param X_train_paths: paths to the training X images 
    :type dir_X: list of Strings 
    :param dim: dimension of the image 
    :type dim: tuple 
    :return newa, newa:
        - newa - height set to images 
        - newa - height set to images 
    :rtype: 
        - newa - integer
        - newa - integer
    """

    a,b = dim
    if (a,b) == (0,0):
        img = imread(X_train_paths[0])
        a0 =  img.shape[0]
        b0 = img.shape[1]
        if a0 != b0:
            raise ValueError("Images are not in sqaure format. Resize or crop them before loading")
        else: 
            if (math.ceil(math.log2(a0)) == math.floor(math.log2(a0))):
                return a0,a0
            else: 
                if (math.log2(a0) - math.floor(math.log2(a0)) < math.ceil(math.log2(a0)) - math.log2(a0)):
                    newa = 2**(math.floor(math.log2(a0)))
                    print("Images were resized to ({newa},{newa})")
                    return newa,newa
                else: 
                    newa = 2**(math.ceil(math.log2(a0)))
                    print("Images were resized to ({newa},{newa})")
                    return newa,newa
    else:
        if a != b:
            raise ValueError("Choose a square format (e.g (512,512) or (128,128))")
        else: 
            if (math.ceil(math.log2(a)) == math.floor(math.log2(a))):
                return a,a
            else: 
                if (math.log2(a) - math.floor(math.log2(a)) < math.ceil(math.log2(a)) - math.log2(a)):
                    newa = 2**(math.floor(math.log2(a)))
                    print("Images were resized to ({newa},{newa})")
                    return newa,newa
                else: 
                    newa = 2**(math.ceil(math.log2(a)))
                    print("Images were resized to ({newa},{newa})")
                    return newa,newa