# https://www.geeksforgeeks.org/python/addition-blending-images-using-opencv-python/
import cv2

# Addition and Blending of images

if __name__ == '__main__':
    img1 = cv2.imread('../_pics/oranges.jpg')
    img2 = cv2.imread('../_pics/strawberry.jpg')

    img = cv2.add(img1, img2)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
