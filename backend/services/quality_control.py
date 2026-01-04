import cv2
import numpy as np

class QualityControlService:
    def __init__(self):
        # Calibration constant: Pixels per Centimeter
        # This needs to be calibrated in real life.
        # Assuming camera is at fixed height viewing a conveyor belt.
        self.pixels_per_cm = 10.0 

    def check_fragile_sticker(self, image: np.ndarray, bbox: list) -> bool:
        """
        Checks for red 'Fragile' stickers within the bounding box using HSV color filtering.
        """
        x1, y1, x2, y2 = map(int, bbox)
        
        # Ensure coordinates are within image bounds
        h, w = image.shape[:2]
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)
        
        roi = image[y1:y2, x1:x2]
        if roi.size == 0:
            return False

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        # Define range for red color (Fragile stickers are usually bright red)
        # Red loops around 180 in HSV, so we need two masks
        lower_red1 = np.array([0, 70, 50])
        upper_red1 = np.array([10, 255, 255])
        
        lower_red2 = np.array([170, 70, 50])
        upper_red2 = np.array([180, 255, 255])
        
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        final_mask = mask1 + mask2
        
        # Calculate percentage of red pixels
        red_pixels = cv2.countNonZero(final_mask)
        total_pixels = roi.shape[0] * roi.shape[1]
        
        if total_pixels == 0: return False
        
        ratio = red_pixels / total_pixels
        
        # If more than 5% of the box is 'Fragile Red', assume sticker is present
        return ratio > 0.05

    def estimate_dimensions(self, bbox: list) -> str:
        """
        Estimates W x H based on bounding box and calibration.
        Returns formatted string "24cm x 15cm"
        """
        x1, y1, x2, y2 = bbox
        width_px = x2 - x1
        height_px = y2 - y1
        
        width_cm = width_px / self.pixels_per_cm
        height_cm = height_px / self.pixels_per_cm
        
        return f"{width_cm:.1f}cm x {height_cm:.1f}cm"

    def detect_defects(self, image: np.ndarray, bbox: list) -> bool:
        """
        Placeholder for defect detection. 
        In a real scenario, this would call a secondary Classification Model (YOLOv8-cls).
        For now, we return False (No defect).
        """
        return False

# Singleton
qc_service = QualityControlService()
