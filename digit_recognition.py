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
        self.data = pd.read_csv('data/train.csv')
        self.create_images()
        print(self.all_images)

    def create_images(self):
        self.all_images = []
        for count, image in self.data.iterrows():
            x = y = 0
            single_image = np.empty([28, 28])
            image_dict = {}
            for key, pixel in enumerate(image):
                if key == 0:
                    image_dict["label"] = pixel
                else:
                    if y == 28:
                        y = 0
                    if x == 28:
                        x = 0
                        y += 1
                    single_image[y][x] = pixel
                    x += 1
            image_dict["image"] = single_image
            self.all_images.append(image_dict)

if __name__ == '__main__':
    obj = digit_recognition()
