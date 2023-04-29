import cv2
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
import pyaudio

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Webcam Streaming"}

@app.get("/video_feed")
@app.get("/video_feed")
async def video_feed(webcam: int = 0):
    video_capture = cv2.VideoCapture(webcam)

    async def generate_frames():
        while True:
            # Capture frame-by-frame
            success, frame = video_capture.read()
            if not success:
                break
            else:
                # Encode the frame in JPEG format
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

                # Yield the frame in byte format
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return StreamingResponse(content=generate_frames(), media_type='multipart/x-mixed-replace; boundary=frame')


@app.get("/cameras")
async def cameras():
    # Get the list of available cameras
    index = 0
    cameras = []
    while True:
        video_capture = cv2.VideoCapture(index)
        if not video_capture.isOpened():
            break
        else:
            # Get the name of the camera as it appears in the operating system
            # name = video_capture.get(cv2.CAP_PROP_DEVICE_NAME)
            cameras.append({"index": index, "name": "Anthony"})
            index += 1
            video_capture.release()

    return {"cameras": cameras}


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == '__main__':
    main()
