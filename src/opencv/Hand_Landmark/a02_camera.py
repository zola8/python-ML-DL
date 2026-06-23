# https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/hand_landmarker/python/hand_landmarker.ipynb
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),  # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),  # Index
    (0, 9), (9, 10), (10, 11), (11, 12),  # Middle
    (0, 13), (13, 14), (14, 15), (15, 16),  # Ring
    (0, 17), (17, 18), (18, 19), (19, 20),  # Pinky
    (5, 9), (9, 13), (13, 17)  # Palm cross-connections
]


def draw_hand_landmarks(frame, hand_landmarks, width, height):
    """
    Extracted method to draw hand landmarks and connections on the frame.
    """
    # Convert normalized coordinates (0.0 to 1.0) to pixel coordinates
    pixel_landmarks = [(int(lm.x * width), int(lm.y * height)) for lm in hand_landmarks]

    # Draw connections (bones)
    for start_idx, end_idx in HAND_CONNECTIONS:
        start_pt = pixel_landmarks[start_idx]
        end_pt = pixel_landmarks[end_idx]
        # cv2.LINE_AA makes the lines look smooth
        cv2.line(frame, start_pt, end_pt, (0, 255, 0), thickness=3, lineType=cv2.LINE_AA)

    # Draw landmarks (joints)
    for x, y in pixel_landmarks:
        cv2.circle(frame, (x, y), 5, (0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)

    return frame


def init_hand_detector():
    # 1. ----- Setup the Hand Landmarker -----
    base_options = python.BaseOptions(model_asset_path='../_data/hand_landmarker.task')
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        num_hands=2,
        # min_hand_detection_confidence=0.5,
        # min_hand_presence_confidence=0.5,
        # min_tracking_confidence=0.5
    )
    return vision.HandLandmarker.create_from_options(options)


def init_cap():
    # 2. ----- Start Video Capture -----
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    return cap


def main():
    detector = init_hand_detector()
    cap = init_cap()

    while cap.isOpened():
        _, frame = cap.read()

        # flip (mirror) frame
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # 3. Convert OpenCV Image (BGR) to MediaPipe Image (RGB)
        # MediaPipe Tasks expects an mp.Image object.
        # We create it from the numpy array, specifying SRGB format.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # 4. Detect Hands
        detection_result = detector.detect(mp_image)

        # 4. Process Results
        if detection_result.hand_landmarks:
            for hand_idx, hand_landmarks in enumerate(detection_result.hand_landmarks):
                # --- PRINTING LANDMARKS ---
                # Example: Print Index Finger Tip (Index 8) for the detected hand
                index_tip = hand_landmarks[8]
                cx = int(index_tip.x * w)
                cy = int(index_tip.y * h)
                print(f"Hand {hand_idx} | Index Tip -> X: {cx}, Y: {cy}")

                # --- DRAWING LANDMARKS ---
                # Call our extracted drawing method
                frame = draw_hand_landmarks(frame, hand_landmarks, w, h)

        # Display the result
        cv2.imshow('MediaPipe Tasks Hand Tracking', frame)

        # exit event handling
        if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
            break

    cap.release()
    cv2.destroyAllWindows()
    detector.close()


if __name__ == '__main__':
    main()
