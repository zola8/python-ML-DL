import cv2
import numpy as np

# Load the image
image = cv2.imread('../_pics/mixed-colors.jpg')

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define lower and upper HSV boundaries for the color blue
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

# Create a mask with cv2.inRange to detect blue colors
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Use bitwise AND to extract the blue color from the original image
result = cv2.bitwise_and(image, image, mask=blue_mask)


cv2.imshow('Color in the image', image)
cv2.imshow('blue mask', blue_mask)
cv2.imshow('where are blues?', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
