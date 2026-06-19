# Python program to explain cv2.cvtColor() method

# importing cv2
import cv2

img = cv2.imread("../_pics/strawberry.jpg", cv2.IMREAD_COLOR)

# Window name in which image is displayed
window_name = 'strawberry'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2GRAY color space
# conversion code
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
