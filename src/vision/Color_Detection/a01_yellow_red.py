import cv2
import numpy as np
from PIL import Image


def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit = hsvC[0][0][0] - 10, 100, 100
    upper_limit = hsvC[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return lower_limit, upper_limit


if __name__ == '__main__':
    yellow = [0, 255, 255]  # BGR values

    cap = cv2.VideoCapture(0)
    # lower_limit, upper_limit = get_limits(color=yellow)

    red_lower = np.array([170, 120, 70])
    red_upper = np.array([180, 255, 255])
    lower_limit, upper_limit = red_lower, red_upper


    while (True):
        ret, frame = cap.read()

        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)
        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()
        if bbox is not None:
            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        cv2.imshow('Color in the image', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
