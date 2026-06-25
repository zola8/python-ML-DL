import os

import cv2

DATA_DIR = "c:/Users/zola/Downloads"
FILENAME = "ALL 5 HEIAN KATA OF SHOTOKAN KARATE (Slow Version) - ULTIMATE KARATE (1080p, h264).mp4"
file_path = os.path.join(DATA_DIR, FILENAME)

if __name__ == '__main__':
    cap = cv2.VideoCapture(file_path)

    frame_count = 0
    max_frames = 200
    # fps = cap.get(cv2.CAP_PROP_FPS)
    # max_frames = int(fps * 10)

    # ----- write -----
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = 10
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(os.path.join(DATA_DIR, 'SlowedVideo.mp4'), fourcc, fps, (width, height))

    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()

        if not ret:
            break  # No more frames → end of video

        cv2.imshow("Video", frame)
        frame_count += 1

        # ----- output -----
        output.write(frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # ----- output -----
    output.release()
    cap.release()
    cv2.destroyAllWindows()
