import numpy as np
import matplotlib as plt
import pandas as pd


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



if __name__ == '__main__':
    obj = digit_recognition()
