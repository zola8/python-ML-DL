import cv2
import numpy as np

img = cv2.imread("../_pics/strawberry.jpg", 0)
cv2.imshow('Original Image', img)


# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
    # Apply gamma correction.
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')

    # cv2.imwrite('gamma_transformed' + str(gamma) + '.jpg', gamma_corrected)
    cv2.imshow(f'Gamma Transformed ({gamma})', gamma_corrected)

cv2.waitKey(0)
cv2.destroyAllWindows()
