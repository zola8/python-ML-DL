# Histogram Equalization (HE) is a technique used to improve image contrast by redistributing pixel intensity values
# across the entire range. It is especially effective in images where the foreground and background have similar brightness,
# making it hard to distinguish details.
# By enhancing areas with low contrast, it makes hidden features more visible, showing finer details in both dark and bright regions.


import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../_pics/strawberry.jpg", 0)

equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))

plt.figure(figsize=(10, 5))
plt.imshow(res, cmap='gray')
plt.title("Original vs Equalized Image")
plt.axis('off')
plt.show()
