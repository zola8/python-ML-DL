# Log transformation expands low-intensity pixel values while compressing higher-intensity values,
# making details in darker regions of an image more visible.

# https://www.geeksforgeeks.org/python/python-intensity-transformation-operations-on-images/

import cv2
import numpy as np

img = cv2.imread("../_pics/strawberry.jpg", 0)

c = 255 / (np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)

log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imshow('Original Image', img)
cv2.imshow('Log Transformed', log_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
