import os

import cv2


def get_sample_filename():
    DATA_DIR = "c:/Users/zola/Downloads"
    FILENAME = "ALL 5 HEIAN KATA OF SHOTOKAN KARATE (Slow Version) - ULTIMATE KARATE (1080p, h264).mp4"
    return os.path.join(DATA_DIR, FILENAME)


def load_video(file_path):
    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    print("Video loaded: ", file_path)
    return cap


def display_frames(cap):
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break  # No more frames → end of video

        cv2.imshow("Video", frame)

        # Press Q to quit
        if cv2.waitKey(fps) & 0xFF == ord('q'):
            break


def get_cap_dim(cap):
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return width, height


def merge_videos(file1_foreground, file2_background, output_path, max_frame_limit=None):
    cap1 = load_video(file1_foreground)
    cap2 = load_video(file2_background)

    width1, height1 = get_cap_dim(cap1)
    width2, height2 = get_cap_dim(cap2)
    if width1 != width2 or height1 != height2:
        print("Error: both videos must have same width and height.")
        exit()

    fps = int(cap2.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width1, height1))

    current_frame = 0
    max_frame = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

    if max_frame_limit is not None:
        max_frame = int(max_frame_limit)

    while current_frame < max_frame:
        ret1, foreground = cap1.read()
        if not ret1:
            cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret1, foreground = cap1.read()

        ret2, background = cap2.read()
        if not ret2:
            break

        merged = cv2.addWeighted(foreground, 0.5, background, 0.5, 0)
        out.write(merged)

        current_frame += 1
        print(f"Frame: {max_frame} / {current_frame}")

    cap1.release()
    cap2.release()
    out.release()


def release_video(cap):
    cap.release()
    cv2.destroyAllWindows()
