import cv2
import numpy as np


def red_frame(frame):
    output = frame.copy()

    # 1. Convert RGB to HSV
    hsv = cv2.cvtColor(output, cv2.COLOR_RGB2HSV)

    # 2. Define TWO ranges for Red because it wraps around the Hue circle

    # Lower range: Hue 0-10
    lower_red_1 = np.array([0, 50, 50])
    upper_red_1 = np.array([10, 255, 255])

    # Upper range: Hue 170-180
    lower_red_2 = np.array([170, 50, 50])
    upper_red_2 = np.array([180, 255, 255])

    # 3. Create masks for both ranges
    mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)

    # 4. Combine the masks using bitwise OR
    final_mask = cv2.bitwise_or(mask_1, mask_2)

    # 5. Apply the combined mask to the original image
    result = cv2.bitwise_and(output, output, mask=final_mask)

    return result


# Green: Lower [35, 50, 50], Upper [85, 255, 255]
# Yellow: Lower [20, 50, 50], Upper [30, 255, 255]

# lower_blue = np.array([100, 50, 50])
# upper_blue = np.array([130, 255, 255])
