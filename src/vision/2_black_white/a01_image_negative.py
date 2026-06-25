import cv2

img = cv2.imread("../_pics/strawberry.jpg", 0)

negative_img = 255 - img

cv2.imshow('Original Image', img)
cv2.imshow('Negative Image', negative_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
