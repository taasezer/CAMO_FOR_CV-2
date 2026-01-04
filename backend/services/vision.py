from ultralytics import YOLO
import cv2
import numpy as np
import threading
from typing import List, Dict

class VisionEngine:
    def __init__(self):
        # Load the nano model for real-time performance
        print("Loading YOLOv8 model...")
        self.model = YOLO("yolov8n.pt") 
        self.lock = threading.Lock()
        self.latest_detections: List[Dict] = []
        
        # We only care about specific classes for logistics
        # 0: person, 39: bottle, 67: cell phone... (COCO dataset)
        # For this prototype we'll track everything but filter in UI or logic if needed.
        # Ideally, we would train a custom model for "cardboard box".
        # For now, we'll assume standard COCO classes.
    
    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        """
        Runs inference on the frame, draws bounding boxes, and updates state.
        Returns the annotated frame.
        """
        results = self.model(frame, verbose=False)
        annotated_frame = results[0].plot()
        
        # Extract detected objects
        detections = []
        for r in results:
            for box in r.boxes:
                # get coordinates
                # x1, y1, x2, y2 = box.xyxy[0]
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                label = self.model.names[cls_id]
                
                detections.append({
                    "label": label,
                    "confidence": conf
                })
        
        with self.lock:
            self.latest_detections = detections
            
        return annotated_frame

    def get_latest_detections(self):
        with self.lock:
            return self.latest_detections

# Singleton
vision_engine = VisionEngine()
