# Thresholding is a foundational technique in computer vision and image processing used to segment objects from the background.
# It works by comparing each pixel value of a grayscale image against a specified threshold value.
# Based on this comparison, pixels are assigned new values, usually 0 (black) or 255 (white).

# OTSU's thresholding is an automatic method that determines the optimal threshold value
# to separate the foreground and background in a grayscale image by maximizing the difference between the two classes.


import cv2


def show_image(img, title):
    # plt.imshow(img, cmap='gray')
    # plt.title(title)
    # plt.axis('off')
    # plt.show()
    cv2.imshow(title, img)


img = cv2.imread("../_pics/strawberry.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

if __name__ == '__main__':
    show_image(gray_image, 'Original Grayscale Image')

    _, thresh_binary = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)
    show_image(thresh_binary, 'Binary Threshold ')

    _, thresh_binary_inv = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY_INV)
    show_image(thresh_binary_inv, 'Binary Threshold Inverted ')

    _, thresh_trunc = cv2.threshold(gray_image, 120, 255, cv2.THRESH_TRUNC)
    show_image(thresh_trunc, 'Truncated Threshold')

    _, thresh_tozero = cv2.threshold(gray_image, 120, 255, cv2.THRESH_TOZERO)
    show_image(thresh_tozero, 'Set to 0 ')

    _, thresh_tozero_inv = cv2.threshold(gray_image, 120, 255, cv2.THRESH_TOZERO_INV)
    show_image(thresh_tozero_inv, 'Set to 0 Inverted')

    thresh_mean = cv2.adaptiveThreshold(
        gray_image, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        199, 5
    )
    show_image(thresh_mean, "Adaptive Mean Thresholding")

    thresh_gauss = cv2.adaptiveThreshold(
        gray_image, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        199, 5
    )
    show_image(thresh_gauss, "Adaptive Gaussian Thresholding")

    ret, otsu_thresh = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print("Calculated Otsu threshold value:", ret)
    show_image(otsu_thresh, "Otsu’s Thresholding")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
