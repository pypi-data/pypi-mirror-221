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


def pullcsv(filename):
    """
    Parses through txt file with values of metrics for epochs and save it as a csv file and returns the name of the csv file
    
    Authors:
        Zhuldyz Ualikhankyzy, Tommy Ciardi 

    :param filename: a txt file with values of metrics for epochs 
    :type filename: string 
    :param dim: dimension of the image 
    :type dim: tuple 
    :return csvname: a name of the csv file with the metrics for each epoch 
    :rtype csvname: string
       
    """

    with open(filename, 'r') as file:
        lines = file.readlines()
    columns = [] 
    for line in lines:
        if line.strip() and (not line.startswith("Epoch")) and ("ETA" not in line) and ("loss" in line):
            columns = re.findall(r' - (\w+):', line)
    df = pd.DataFrame(columns=columns)
    row_index = 0
    for line in lines:
        if line.strip() and (not line.startswith("Epoch")) and ("ETA" not in line) and ("loss" in line):
            numbers = [float(x) for x in re.findall(r':\s(.*?)(?:\s-|$)', line)]
            df.loc[row_index] = numbers
            row_index = row_index+1
    df.to_csv(re.findall(r'\d+', filename)[0] + "epochs_metrics.csv",index=True)
    csvname = re.findall(r'\d+', filename)[0] + "epochs_metrics.csv"
    return csvname