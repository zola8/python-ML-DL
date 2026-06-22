import os
import pickle

import mediapipe as mp
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python.vision import HandLandmarkerResult
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode

DATA_DIR = './data'

if __name__ == '__main__':
    base_options = BaseOptions(model_asset_path='../../_data/hand_landmarker.task')
    options = mp.tasks.vision.HandLandmarkerOptions(base_options=base_options,
                                                    running_mode=VisionTaskRunningMode.IMAGE,
                                                    num_hands=2)
    detector = mp.tasks.vision.HandLandmarker.create_from_options(options)

    data = []
    labels = []

    for dir_ in os.listdir(DATA_DIR):
        for img_filename in os.listdir(os.path.join(DATA_DIR, dir_)):
            print("\nImage: ", os.path.join(DATA_DIR, dir_, img_filename))
            image = mp.Image.create_from_file(os.path.join(DATA_DIR, dir_, img_filename))
            detection_result: HandLandmarkerResult = detector.detect(image)
            # print(detection_result)

            data_aux = []
            x_ = []
            y_ = []

            for hand_landmarks in detection_result.hand_landmarks:
                for i in range(len(hand_landmarks)):
                    x = hand_landmarks[i].x
                    y = hand_landmarks[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks)):
                    x = hand_landmarks[i].x
                    y = hand_landmarks[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(dir_)

    f = open('data.pickle', 'wb')
    pickle.dump({'data': data, 'labels': labels}, f)
    f.close()

# https://www.youtube.com/watch?v=MJCSjXepaAM
# https://github.com/computervisioneng/sign-language-detector-python/blob/master/create_dataset.py

# https://www.youtube.com/watch?v=o_MGqeFMAGE&pp=ugUEEgJlbg%3D%3D
