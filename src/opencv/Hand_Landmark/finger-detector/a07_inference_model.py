import pickle

import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode

from src.opencv.hand_landmark.a01_image import draw_landmarks_on_image

labels_dict = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5'}

mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles


def main():
    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

    base_options = BaseOptions(model_asset_path='../../_data/hand_landmarker.task')
    options = mp.tasks.vision.HandLandmarkerOptions(base_options=base_options,
                                                    running_mode=VisionTaskRunningMode.IMAGE,
                                                    num_hands=1)
    detector = mp.tasks.vision.HandLandmarker.create_from_options(options)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        detection_result = detector.detect(mp_image)

        annotated_image = draw_landmarks_on_image(frame, detection_result)

        if detection_result.hand_landmarks:
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

            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = labels_dict[int(prediction[0])]

            # print(prediction, predicted_character)

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(annotated_image, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0),
                        3, cv2.LINE_AA)

        cv2.imshow('frame', annotated_image)

        if cv2.waitKey(5) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
