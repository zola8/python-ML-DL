import cv2
from ultralytics import YOLO

# 1. Load your specific model
# Ensure 'yolo26n.pt' is in your current working directory or provide the full path
model_path = "yolo26n.pt"
try:
    model = YOLO(model_path)
except Exception as e:
    print(f"Error loading model: {e}")
    print("Make sure 'yolo26n.pt' exists in your directory or provide the correct path.")
    exit()

# 2. Initialize the camera
# cap = cv2.VideoCapture(r'c:\Users\zola\Downloads\Montreal Walking Tours (1080p, h264).mp4')
cap = cv2.VideoCapture(0)



if __name__ == '__main__':

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # write
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = 24 # int(cap.get(cv2.CAP_PROP_FPS) * 4)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(('test_yolo3.mp4'), fourcc, fps, (width, height))


    while True:
        # 3. Read frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # 4. Run inference
        # verbose=False keeps the console clean
        results = model(frame, verbose=False)

        # 5. Process and draw results
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Extract coordinates
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Extract class ID and confidence
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])

                # Get class name from model's names dictionary
                class_name = model.names[cls_id]

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Draw label
                label = f"{class_name} {conf:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 6. Display the result
        cv2.imshow('YOLO Detection (yolo26n)', frame)
        output.write(frame)

        # Break on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    output.release()
    cap.release()
    cv2.destroyAllWindows()
