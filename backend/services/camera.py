import cv2
import threading
from typing import Generator

class CameraService:
    def __init__(self, camera_id: int):
        self.camera_id = camera_id
        self.camera = cv2.VideoCapture(camera_id)
        self.lock = threading.Lock()
    
    def generate_frames(self) -> Generator[bytes, None, None]:
        while True:
            with self.lock:
                if not self.camera.isOpened():
                    break
                success, frame = self.camera.read()
                if not success:
                    break
                
                # Encode frame to JPEG
                ret, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()
            
            # Yield frame for MJPEG stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

# Singleton instance for global access
# We'll initialize this properly in the main app lifecycle
camera_manager = CameraService(0)
