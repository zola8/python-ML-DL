# https://www.youtube.com/watch?v=t71sQ6WY7L4

import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

# 1. Disable Auto White Balance (0 = off, 1 = on)
cap.set(cv2.CAP_PROP_AUTO_WB, 0)

# 2. Set a manual White Balance Temperature (in Kelvin)
# 4000-4600 is usually good for indoor/office lighting.
# 5000-5500 is closer to daylight. You may need to tweak this number.
cap.set(cv2.CAP_PROP_WB_TEMPERATURE, 4600)

# Optional: Disable Auto Exposure if it's also causing issues
# Note: The value for manual exposure varies by OS.
# For Windows (DirectShow), 0.25 is usually manual. For Linux (V4L2), 1 is manual.
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)


if __name__ == '__main__':
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        # middle point of the screen, pick pixel value
        cx, cy = int(width / 2), int(height / 2)
        pixel_center = hsv_frame[cx, cy]
        hue_value = pixel_center[0]

        color = "Undefined"
        if hue_value < 5:
            color = "Red"
        elif hue_value < 22:
            color = "Orange"
        elif hue_value < 33:
            color = "Yellow"
        elif hue_value < 78:
            color = "Green"
        elif hue_value < 131:
            color = "Blue"
        elif hue_value < 167:
            color = "Violet"
        else:
            color = "Red"

        cv2.putText(frame, color, [10, 50], cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
        cv2.circle(frame, (cx, cy), 10, (255, 0, 0), 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
