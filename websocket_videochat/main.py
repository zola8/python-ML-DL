# https://github.com/MohdSakib535/FastApi_WebRTC/blob/master/README.md

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from websocket_videochat.routers import webrtc

app = FastAPI(title="WebRTC FastAPI Video Chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

app.include_router(webrtc.router)


@app.get("/")
async def read_root():
    return FileResponse(os.path.join(static_path, "index.html"))


@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "WebRTC server is running"}


if __name__ == "__main__":
    import uvicorn

    print("http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001)
