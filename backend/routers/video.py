from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from backend.services.camera import camera_manager

router = APIRouter(
    prefix="/video",
    tags=["Video Stream"]
)

@router.get("/feed")
def video_feed():
    return StreamingResponse(camera_manager.generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")
