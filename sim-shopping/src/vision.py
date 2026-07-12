import cv2
from ultralytics import YOLO

model = YOLO("yolo26n.pt")


def process_frame(frame, cart: list):
    if frame is None:
        return None, "Waiting for camera...", cart

    output = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    return output, f"Live @ ~5 FPS", cart
