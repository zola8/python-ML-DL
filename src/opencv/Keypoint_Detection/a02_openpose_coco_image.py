import cv2
import numpy as np

# Load MATCHING COCO files
net = cv2.dnn.readNetFromCaffe(
    '../_data/openpose_pose_coco.prototxt',
    '../_data/pose_iter_440000.caffemodel'
)

# COCO has 18 keypoints
BODY_PARTS = {
    "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
    "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
    "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
    "LEye": 15, "REar": 16, "LEar": 17
}

POSE_PAIRS = [
    ["Neck", "RShoulder"], ["Neck", "LShoulder"],
    ["RShoulder", "RElbow"], ["RElbow", "RWrist"],
    ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
    ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"],
    ["Neck", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"],
    ["Neck", "Nose"], ["Nose", "REye"], ["REye", "REar"],
    ["Nose", "LEye"], ["LEye", "LEar"]
]


def process_frame(frame):
    frame_height, frame_width = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        frame, 1.0 / 255, (368, 368), (0, 0, 0), swapRB=False, crop=False
    )
    net.setInput(blob)
    output = net.forward()  # ← Should work now

    points = []
    for i in range(len(BODY_PARTS)):
        prob_map = output[0, i, :, :]
        _, max_val, _, max_loc = cv2.minMaxLoc(prob_map)

        x = (frame_width * max_loc[0]) / output.shape[3]
        y = (frame_height * max_loc[1]) / output.shape[2]

        if max_val > 0.1:
            points.append((int(x), int(y)))
            cv2.circle(frame, (int(x), int(y)), 8, (0, 255, 255), -1, cv2.FILLED)
        else:
            points.append(None)

    for pair in POSE_PAIRS:
        p1, p2 = BODY_PARTS[pair[0]], BODY_PARTS[pair[1]]
        if points[p1] and points[p2]:
            cv2.line(frame, points[p1], points[p2], (0, 255, 0), 3)

    return frame


# img = cv2.imread('../_pics/finger2.jpg')
img = cv2.imread('../_pics/karate1.png')
result = process_frame(img)
cv2.imshow('Pose', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
