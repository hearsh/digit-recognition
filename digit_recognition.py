import numpy as np
import matplotlib as plt
import pandas as pd
import itertools

from keras.utils.np_utils import to_categorical # convert to one-hot-encoding
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau


class digit_recognition(object):
    """
    Code to read data for digit recognition
    """
    def __init__(self):
        """
        This Method is always called first
        Initialize all values here
        """
        self.train = pd.read_csv('data/train.csv')
        self.test = pd.read_csv('data/test.csv')
    def preprocessing(self):
        """
        This method preprocesses the images.
        Normalizing, Reshaping, and encoding them for Keras
        :return:
        """
        Y_train = self.train['label']
        X_train = self.train.drop(labels=['label'],axis=1)
        X_train = X_train/255.0
        self.test = self.test/255.0
        X_train = X_train.values.reshape(-1, 28, 28, 1)
        self.test = self.test.values.reshape(-1, 28, 28, 1)

if __name__ == '__main__':
    obj = digit_recognition()
