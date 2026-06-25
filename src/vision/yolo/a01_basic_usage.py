import os

from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # pretrained YOLO26n model

if __name__ == '__main__':

    images = [
        "animals.jpg",
        "kitchen1.jpg",
        "kitchen2.jpg",
        "mixed.jpg",
        "people.jpg",
    ]

    list_of_images = [os.path.join("", "_pics", name) for name in images]
    print(list_of_images)

    # Run batched inference on a list of images
    results = model(list_of_images)  # return a list of Results objects

    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs

        result.show()  # display to screen
        # result.save(filename="result.jpg")  # save to disk
