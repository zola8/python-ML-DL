import cv2
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

app = FastAPI()

# Allow Streamlit (running on a different port) to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the camera (0 is usually the default webcam)
# Note: If you don't have a webcam, replace 0 with a video file path like "video.mp4"
camera = cv2.VideoCapture(0)


def generate_frames():
    """Generator that reads from the camera and yields MJPEG frames."""
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Yield the frame in MJPEG format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.get("/video_feed")
async def video_feed():
    """Endpoint that streams the MJPEG video."""
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    print("Starting FastAPI backend on http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001)
