import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# --- CONFIGURATION ---
PERSON_CLASS_INDEX = 15  # Change this based on your debug output
BLUR_INTENSITY = 51  # Odd number. Higher = more blurry background (e.g., 21, 51, 99)
EDGE_SMOOTHNESS = 15  # Odd number. Higher = softer transition edge (e.g., 5, 15, 31)


# ---------------------

def show_webcam():
    # Create the image segmenter
    with vision.ImageSegmenter.create_from_options(options) as segmenter:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)

            # 1. Convert BGR -> RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

            # 2. Run segmentation
            segmentation_result = segmenter.segment(mp_image)

            if segmentation_result.category_mask:
                # 3. Extract and flatten the mask to 2D (H, W)
                raw_mask = segmentation_result.category_mask.numpy_view()
                mask_2d = np.squeeze(raw_mask)

                # 4. KEY FIX: Convert category indices to a binary mask (0.0 or 1.0)
                # Pixels matching PERSON_CLASS_INDEX become 1.0 (foreground), else 0.0
                binary_mask = (mask_2d == PERSON_CLASS_INDEX).astype(np.float32)

                # 5. Expand to 3 channels: (H, W) -> (H, W, 3)
                mask_3d = np.stack([binary_mask] * 3, axis=-1)

                # 6. Optional: soften edges for a smoother blend
                # Apply edge smoothing to the mask
                if EDGE_SMOOTHNESS > 1:
                    mask_3d = cv2.GaussianBlur(mask_3d, (EDGE_SMOOTHNESS, EDGE_SMOOTHNESS), 0)

                # 7. Blur the entire frame
                blurred_frame = cv2.GaussianBlur(frame, (BLUR_INTENSITY, BLUR_INTENSITY), 0)

                # 8. Composite: foreground sharp, background blurred
                # Now mask values are strictly 0.0-1.0, so colors stay correct
                result = (frame * mask_3d + blurred_frame * (1 - mask_3d)).astype(np.uint8)

                cv2.imshow('webcam blurred background test', result)
            else:
                cv2.imshow('webcam', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    _, frame = cap.read()
    print(f"Resolution: {frame.shape[1]} x {frame.shape[0]}")

    # Create the options that will be used for ImageSegmenter
    base_options = python.BaseOptions(model_asset_path='deeplab_v3.tflite')
    options = vision.ImageSegmenterOptions(base_options=base_options,
                                           output_category_mask=True)

    show_webcam()

    cap.release()
    cv2.destroyAllWindows()
