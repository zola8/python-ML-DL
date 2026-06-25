# Image translation is the process of shifting an image from one position to another.
# We simply move the entire image by a fixed number of pixels, either horizontally (along the x-axis)
# or vertically (along the y-axis).
# This technique is important in various computer vision tasks such as object tracking,
# image alignment and creating animations.
# We achieve this by using a transformation matrix which helps shift the image without distorting its content.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../_pics/strawberry.jpg", cv2.IMREAD_COLOR_RGB)

rows, cols, _ = img.shape

M_left = np.float32([[1, 0, -50], [0, 1, 0]])
M_right = np.float32([[1, 0, 50], [0, 1, 0]])
M_top = np.float32([[1, 0, 0], [0, 1, 50]])
M_bottom = np.float32([[1, 0, 0], [0, 1, -50]])

img_left = cv2.warpAffine(img, M_left, (cols, rows))
img_right = cv2.warpAffine(img, M_right, (cols, rows))
img_top = cv2.warpAffine(img, M_top, (cols, rows))
img_bottom = cv2.warpAffine(img, M_bottom, (cols, rows))

plt.subplot(221), plt.imshow(img_left), plt.title('Left')
plt.subplot(222), plt.imshow(img_right), plt.title('Right')
plt.subplot(223), plt.imshow(img_top), plt.title('Top')
plt.subplot(224), plt.imshow(img_bottom), plt.title('Bottom')
plt.show()
