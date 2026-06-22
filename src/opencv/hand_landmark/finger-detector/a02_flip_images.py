import os

import cv2

DATA_DIR = './data'
number_of_classes = 5
dataset_size = 100


if __name__ == '__main__':
    for i in range(number_of_classes):
        for j in range(dataset_size):
            file_path = os.path.join(DATA_DIR, str(i), str(j) + '.jpg')
            src = cv2.imread(file_path)
            image = cv2.flip(src, 1)
            cv2.imwrite(file_path, image)

    print('done')
