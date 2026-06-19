import cv2

# Read image from disk.
img = cv2.imread('../_pics/oranges.jpg')

# Canny edge detection.
edges = cv2.Canny(img, 100, 200)

# Write image back to disk.
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
