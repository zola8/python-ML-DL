# Python program to illustrate
# arithmetic operation of
# addition of two images

# organizing imports
import cv2

# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread('../_pics/apple.jpg')
image2 = cv2.imread('../_pics/oranges.jpg')

image1 = cv2.resize(image1, (1000, 1000))
image2 = cv2.resize(image2, (1000, 1000))

# cv2.subtract is applied over the
# image inputs with applied parameters
sub = cv2.subtract(image1, image2)

# the window showing output image
# with the subtracted image
cv2.imshow('Subtracted Image', sub)


# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
