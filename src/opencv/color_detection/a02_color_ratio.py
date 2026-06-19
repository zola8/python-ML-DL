import cv2
import numpy as np


def colorDetection(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    '''Red'''
    # Range for lower red
    red_lower = np.array([0, 120, 70])
    red_upper = np.array([10, 255, 255])
    mask_red1 = cv2.inRange(hsv, red_lower, red_upper)

    # Range for upper range
    red_lower = np.array([170, 120, 70])
    red_upper = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(hsv, red_lower, red_upper)

    mask_red = mask_red1 + mask_red2

    red_output = cv2.bitwise_and(image, image, mask=mask_red)
    red_ratio = (cv2.countNonZero(mask_red)) / (image.size / 3)

    print("Red in image", np.round(red_ratio * 100, 2))

    '''yellow'''
    # Range for upper range
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    yellow_output = cv2.bitwise_and(image, image, mask=mask_yellow)
    yellow_ratio = (cv2.countNonZero(mask_yellow)) / (image.size / 3)

    print("Yellow in image", np.round(yellow_ratio * 100, 2))


if __name__ == '__main__':
    image = cv2.imread("../_pics/strawberry.jpg")
    colorDetection(image)
