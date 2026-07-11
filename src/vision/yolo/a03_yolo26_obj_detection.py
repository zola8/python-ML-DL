from ultralytics import YOLO

if __name__ == '__main__':
    # Load the latest YOLO26n model (nano version for speed)
    model = YOLO("yolo26n.pt")

    # Run inference on an image from a URL
    results = model("../_pics/people.jpg")

    # Display the results with bounding boxes
    results[0].show()
