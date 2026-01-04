import cv2
import threading
from typing import Generator

from backend.services.vision import vision_engine

class CameraService:
    def __init__(self, camera_id: int):
        self.camera_id = camera_id
        self.camera = cv2.VideoCapture(camera_id)
        self.lock = threading.Lock()
        self.last_frame = None

    def get_snapshot(self):
        with self.lock:
            if self.last_frame is not None:
                return self.last_frame.copy()
            return None
    
    def generate_frames(self) -> Generator[bytes, None, None]:
        while True:
            with self.lock:
                if not self.camera.isOpened():
                    break
                success, frame = self.camera.read()
                if not success:
                    break
                
                self.last_frame = frame
                
                # --- AI PROCESSING ---
                # Pass frame through YOLOv8
                annotated_frame = vision_engine.process_frame(frame)
                # ---------------------

                # Encode processed frame to JPEG
                ret, buffer = cv2.imencode('.jpg', annotated_frame)
                frame_bytes = buffer.tobytes()
            
            # Yield frame for MJPEG stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

# Singleton instance for global access
camera_manager = CameraService(0)
