from fastapi import FastAPI, UploadFile, File
import pytesseract
import cv2
import os
import ctypes

# C# DLL'sini yükle
cpp_dll = ctypes.CDLL('./CAMO_CM_CPP.dll')

app = FastAPI()


@app.post("/upload")
async def upload_cargo(file: UploadFile = File(...)):
    video_path = f"temp/{file.filename}"
    with open(video_path, "wb") as f:
        f.write(await file.read())

    # OCR ile etiket oku
    frame = cv2.imread(video_path)
    label = pytesseract.image_to_string(frame)

    # C++ fonksiyonunu çağır
    cpp_dll.captureVideo(video_path)

    # Veritabanına kaydet
    db_manager = DatabaseManager()
    db_manager.SaveCargoInfo("KGO-123", video_path, label)

    return {"message": "Kargo kaydedildi!"}
