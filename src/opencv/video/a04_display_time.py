import datetime

import cv2

from src.opencv.video.video_commons import get_sample_filename

if __name__ == '__main__':

    vid = cv2.VideoCapture(get_sample_filename())

    while vid.isOpened():
        ret, frame = vid.read()
        if not ret:
            break

        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        dt = str(datetime.datetime.now())
        frame = cv2.putText(frame, dt,
                            (10, 100),  # Position (x, y)
                            font, 1,  # Font and scale
                            (210, 155, 155),  # Color (B, G, R)
                            2,  # Thickness
                            cv2.LINE_8)  # Line type

        cv2.imshow('Video with Date & Time', frame)

        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:  # Quit on 'q' or ESC
            break

    vid.release()
    cv2.destroyAllWindows()
