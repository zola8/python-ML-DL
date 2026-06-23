import os

import cv2

DATA_DIR = "c:/Users/zola/Downloads"
FILENAME = "ALL 5 HEIAN KATA OF SHOTOKAN KARATE (Slow Version) - ULTIMATE KARATE (1080p, h264).mp4"
file_path = os.path.join(DATA_DIR, FILENAME)

if __name__ == '__main__':
    cap = cv2.VideoCapture(file_path)

    frame_count = 0
    max_frames = 200

    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if not ret:
            break

        cv2.imshow("Video", gray)
        frame_count += 1

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # ----- output -----
    cap.release()
    cv2.destroyAllWindows()
