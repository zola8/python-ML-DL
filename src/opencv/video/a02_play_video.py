import datetime

import cv2

from src.opencv.video.video_commons import load_video, display_frames, release_video, get_sample_filename

if __name__ == '__main__':
    file_path = get_sample_filename()
    cap = load_video(file_path)

    # video details:
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    seconds = round(frames / fps, 3)
    video_time = datetime.timedelta(seconds=seconds)

    print(f"Frames: {frames}")
    print(f"FPS: {fps}")
    print(f"Duration in seconds: {seconds}")
    print(f"Video time (HH:MM:SS): {video_time}")

    display_frames(cap)

    release_video(cap)
