import cv2
from ultralytics import YOLO

# model = YOLO("yolo26n.pt")
model = YOLO("yolov8n-oiv7.pt")


def process_frame(frame_raw, cart: list):
    if frame_raw is None:
        return None, "Waiting for camera...", cart

    frame = frame_raw.copy()

    # results = model(frame, verbose=False, conf=0.6)
    results = model(frame)

    for result in results:
        for detection in result.boxes:
            class_id = int(detection.cls[0])
            class_name = model.names[class_id]

            x1, y1, x2, y2 = detection.xyxy[0].cpu().numpy().astype(int)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            label = f"{class_name}: {detection.conf[0]:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame, f"Live @ ~5 FPS", cart
