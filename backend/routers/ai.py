from fastapi import APIRouter
from backend.services.vision import vision_engine

router = APIRouter(
    prefix="/ai",
    tags=["AI Analytics"]
)

@router.get("/detections")
def get_detections():
    """
    Returns the list of currently detected objects.
    """
    return {"detections": vision_engine.get_latest_detections()}

@router.post("/scan-text")
def scan_text():
    """
    Captures the current frame and runs OCR on it.
    """
    from backend.services.camera import camera_manager
    from backend.services.ocr import ocr_engine
    
    frame = camera_manager.get_snapshot()
    if frame is None:
        return {"error": "Camera not active"}
    
    text_results = ocr_engine.extract_text(frame)
    return {"text": text_results}
