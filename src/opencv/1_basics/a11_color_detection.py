# Detecting Red Color in an Image Using HSV
# https://www.geeksforgeeks.org/python/color-spaces-in-opencv-python/

import cv2
import numpy as np

image = cv2.imread("../_pics/strawberry.jpg")

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

mask = cv2.inRange(image_hsv, lower_red, upper_red)

result = cv2.bitwise_and(image, image, mask=mask)

if __name__ == '__main__':
    cv2.imshow('Detecting red color', result)

    B, G, R = cv2.split(image)
    cv2.imshow("image", image)

    cv2.imshow("B", B)

    cv2.imshow("G", G)

    cv2.imshow("R", R)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
