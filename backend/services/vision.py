from ultralytics import YOLO
import cv2
import numpy as np
import threading
from typing import List, Dict
from backend.services.quality_control import qc_service

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
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                label = self.model.names[cls_id]

                # --- QUALITY CONTROL CHECKS ---
                # Only run on 'suitcase', 'backpack', 'handbag', 'crate' or generic objects that look like packages
                # In COCO, 'suitcase' is close to a box. 'cup', 'bowl' etc are not.
                # For demo, we run on EVERYTHING.
                
                is_fragile = qc_service.check_fragile_sticker(frame, [x1, y1, x2, y2])
                dimensions = qc_service.estimate_dimensions([x1, y1, x2, y2])
                
                # Annotate frame with QC Data
                if is_fragile:
                    cv2.putText(annotated_frame, "FRAGILE", (int(x1), int(y1)-10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
                    
                cv2.putText(annotated_frame, dimensions, (int(x1), int(y2)+20), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

                detections.append({
                    "label": label,
                    "confidence": conf,
                    "is_fragile": is_fragile,
                    "dimensions": dimensions
                })
        
        with self.lock:
            self.latest_detections = detections
            
        return annotated_frame

    def get_latest_detections(self):
        with self.lock:
            return self.latest_detections

# Singleton
vision_engine = VisionEngine()
