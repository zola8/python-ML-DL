import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.vision import ImageSegmenterOptions, ImageSegmenter

cap = cv2.VideoCapture(0)
base_options = python.BaseOptions(model_asset_path='deeplab_v3.tflite')
options = ImageSegmenterOptions(base_options=base_options, output_category_mask=True)

with ImageSegmenter.create_from_options(options) as segmenter:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = segmenter.segment(mp_image)

    mask = np.squeeze(result.category_mask.numpy_view())
    print("Mask shape:", mask.shape)
    print("Unique class indices found:", np.unique(mask))
    # print("Colormap (index -> label):", result.category_mask.colormap if hasattr(result, 'category_mask') else "N/A")

cap.release()
