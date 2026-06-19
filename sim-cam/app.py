import cv2
import gradio as gr
import numpy as np

css = """
    footer {visibility: hidden}
    .tight_layout {margin: 1em 0}
    .tight_next {margin-bottom: 1.5em}
"""


def process_frame(frame, filter_type):
    """
    Processes the frame based on the selected filter.
    Note: Gradio passes webcam images as RGB numpy arrays.
    """
    if frame is None:
        return None

    # Make a copy to avoid modifying the original input directly if not needed
    output = frame.copy()

    if filter_type == "Original":
        return output
    elif filter_type == "Grayscale":
        gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    elif filter_type == "Red Filter":
        # 1. Convert RGB to HSV
        hsv = cv2.cvtColor(output, cv2.COLOR_RGB2HSV)

        # 2. Define TWO ranges for Red because it wraps around the Hue circle

        # Lower range: Hue 0-10
        lower_red_1 = np.array([0, 50, 50])
        upper_red_1 = np.array([10, 255, 255])

        # Upper range: Hue 170-180
        lower_red_2 = np.array([170, 50, 50])
        upper_red_2 = np.array([180, 255, 255])

        # 3. Create masks for both ranges
        mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
        mask_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)

        # 4. Combine the masks using bitwise OR
        final_mask = cv2.bitwise_or(mask_1, mask_2)

        # 5. Apply the combined mask to the original image
        result = cv2.bitwise_and(output, output, mask=final_mask)

        return result

    elif filter_type == "Edge Detection":
        edges = cv2.Canny(output, 100, 200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    elif filter_type == "Gaussian Blur":
        return cv2.GaussianBlur(output, (21, 21), 0)
    elif filter_type == "Invert Colors":
        return 255 - output
    else:
        return output


# Define the options for the dropdown
filter_options = [
    "Original",
    "Grayscale",
    "Red Filter",
    "Edge Detection",
    "Gaussian Blur",
    "Invert Colors"
]

# Create the Gradio Interface
demo = gr.Interface(
    fn=process_frame,
    inputs=[
        gr.Image(sources="webcam", streaming=True, label="Live Camera"),
        gr.Dropdown(choices=filter_options, value="Original", label="Select Filter")
    ],
    outputs=gr.Image(type="numpy", label="Processed Output"),
    live=True,  # This enables the real-time continuous streaming
    title="Real-Time Camera with Image Processing",
    description="A real-time webcam feed. Select a filter from the dropdown to change the effect!",
    flagging_mode="never"
)

if __name__ == '__main__':
    print("Local URL: http://localhost:7860")
    demo.queue()
    demo.launch(
        css=css,
        server_name="0.0.0.0",
        server_port=7860,
    )
