import os

import cv2
import numpy as np
from matplotlib import pyplot as plt
from pyzbar.pyzbar import decode


def list_images_info(image_path='../_pics/'):
    for j in sorted(os.listdir(image_path)):
        img = cv2.imread(os.path.join(image_path, j))
        qr_info = decode(img)

        if len(qr_info) == 0:
            continue

        print(j, len(qr_info))

        for qr in qr_info:
            print("\t", qr.data)
            rect = qr.rect
            polygon = qr.polygon
            img = cv2.rectangle(
                img,
                (rect.left, rect.top),
                (rect.left + rect.width, rect.top + rect.height),
                (0, 255, 0),
                5
            )
            img = cv2.polylines(img, np.array([polygon]), True, (255, 0, 0), 5)

            plt.imshow(img)
            plt.show()


if __name__ == '__main__':
    print('How many QR codes are on the picture?')
    list_images_info()
