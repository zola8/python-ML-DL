import cv2

img = cv2.imread("../_pics/strawberry.jpg")

image = cv2.copyMakeBorder( img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))

cv2.imshow("Bordered Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
