from pprint import pprint

from ultralytics import YOLO

if __name__ == '__main__':
    # Load model 26
    # model = YOLO("yolo26n.pt")

    # View the class names list
    # pprint(model.names)

    # Load an Open Images V7 pretrained YOLOv8n model
    model = YOLO("yolov8n-oiv7.pt")
    pprint(model.names)

    # model = YOLO("yolov10n.pt")
    # pprint(model.names)
