import os

import cv2

from src.opencv.video.video_commons import get_sample_filename


def mouse_click(event, x, y, flags, param):
    # to check if left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        print("left click", x, y)
        # cv2.imwrite("frame.jpg", param)

    # to check if right mouse button was clicked
    if event == cv2.EVENT_RBUTTONDOWN:
        print("right click", x, y)
        cv2.imshow("Current Frame", param)


if __name__ == '__main__':
    cap = cv2.VideoCapture(get_sample_filename())

    if not cap.isOpened():
        # give error message
        print("Error in opening file.")
    else:
        # proceed forward
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow("Video", frame)
                cv2.setMouseCallback('Video', mouse_click, param=frame)
                if cv2.waitKey(24) & 0xFF == ord('q'):
                    break
            else:
                break

    cap.release()
    cv2.destroyAllWindows()
