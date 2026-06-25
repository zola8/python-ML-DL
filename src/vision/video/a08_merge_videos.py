from src.opencv.video.video_commons import merge_videos

path_1 = "../_pics/z.mp4"
path_2 = "c:/Users/zola/Downloads/ALL 5 HEIAN KATA OF SHOTOKAN KARATE (Slow Version) - ULTIMATE KARATE (1080p, h264).mp4"
path_3 = "c:/Users/zola/Downloads/Recording 2026-06-22 193144.mp4"
path_output = "c:/Users/zola/Downloads/merge.mp4"

if __name__ == '__main__':
    merge_videos(path_1, path_2, path_output, None)
