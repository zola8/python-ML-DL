# https://www.geeksforgeeks.org/python/convert-python-script-to-exe-file/
# https://pyinstaller.org/en/stable/usage.html

import cv2

cap = cv2.VideoCapture(0)


def show_webcam():
    print('Webcam started')
    while True:
        _, frame = cap.read()

        cv2.imshow('webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    show_webcam()

    cap.release()
    cv2.destroyAllWindows()

# pyinstaller a01.py -> build, dist (exe) folders
