import cv2


def show_webcam():
    while cap.isOpened():
        ret, frame = cap.read()

        cv2.imshow('webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

    show_webcam()

    cap.release()
    cv2.destroyAllWindows()
