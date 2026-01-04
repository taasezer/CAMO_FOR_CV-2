import easyocr
import numpy as np
import threading

class OCREngine:
    def __init__(self):
        print("Loading OCR Engine...")
        # 'tr' for Turkish, 'en' for English
        self.reader = easyocr.Reader(['tr', 'en'], gpu=False, verbose=False) 
        self.lock = threading.Lock()
    
    def extract_text(self, image: np.ndarray) -> list[str]:
        """
        Extracts raw text from the image.
        """
        with self.lock:
            # detail=0 returns just the text list
            result = self.reader.readtext(image, detail=0)
        return result

# Singleton
ocr_engine = OCREngine()
