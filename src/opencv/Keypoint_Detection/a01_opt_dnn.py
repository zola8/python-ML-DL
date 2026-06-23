import cv2

BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
              "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
              "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
              ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
              ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
              ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]


def pose_detector(frame, threshold=0.2):
    frame_width, frame_height = frame.shape[1], frame.shape[0]
    net.setInput(cv2.dnn.blobFromImage(frame, 1.0, (frame_width, frame_height), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()
    out = out[:, :19, :, :]

    points = []
    for i in range(len(BODY_PARTS)):
        heat_map = out[0, i, :, :]
        _, conf, _, point = cv2.minMaxLoc(heat_map)
        x = int((frame_width * point[0]) / out.shape[3])
        y = int((frame_height * point[1]) / out.shape[2])
        points.append((x, y) if conf > threshold else None)

    for pair in POSE_PAIRS:
        part_from, part_to = pair
        id_from, id_to = BODY_PARTS[part_from], BODY_PARTS[part_to]
        if points[id_from] and points[id_to]:
            cv2.line(frame, points[id_from], points[id_to], (0, 255, 0), 3)
            cv2.ellipse(frame, points[id_from], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED)
            cv2.ellipse(frame, points[id_to], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED)
    return frame



if __name__ == '__main__':
    net = cv2.dnn.readNetFromTensorflow("graph_opt.pb")
    # cap = cv2.VideoCapture(0)
    #
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     frame = cv2.flip(frame, 1)
    #
    #     output_frame = pose_detector(frame)
    #
    #     cv2.imshow('frame', output_frame)
    #
    #     if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
    #         break
    #
    # cap.release()
    # cv2.destroyAllWindows()

    img = cv2.imread('../_pics/finger2.jpg')
    output_frame = pose_detector(img)
    cv2.imshow('output_frame', output_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
