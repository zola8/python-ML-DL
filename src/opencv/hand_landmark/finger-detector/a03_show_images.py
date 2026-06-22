import os

import cv2
import matplotlib.pyplot as plt

DATA_DIR = './data'

if __name__ == '__main__':

    for dir_ in os.listdir(DATA_DIR):
        for img_filename in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:
            # for img_filename in os.listdir(os.path.join(DATA_DIR, dir_)):
            # print(dir_, img_path)

            img = cv2.imread(os.path.join(DATA_DIR, dir_, img_filename))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            plt.figure()
            plt.imshow(img_rgb)

    plt.show()
