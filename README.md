
# CAMO_FOR_CV-2

This project is an advanced, AI-powered cargo tracking and verification system. It leverages computer vision to automate the packing process, verify shipment integrity, and provide real-time operational analytics.

## About the Project

CAMO_FOR_CV-2 modernizes traditional logistics tracking by replacing manual checks with intelligent automation. The system uses a camera feed to detect packages, read shipping labels, and verify compliance (such as "Fragile" warnings) without human intervention.

## Key Features

### Intelligent Vision
*   **Object Detection:** Uses YOLOv8 to automatically identify boxes, personnel, and equipment in the video feed.
*   **Automatic Recording:** Triggers video recording only when relevant objects are detected, optimizing storage.

### Text Recognition (OCR)
*   **Label Reading:** Integrated EasyOCR engine scans and digitizes text from shipping labels.
*   **Data Extraction:** Automatically parses names, addresses, and tracking numbers from valid labels.

### Quality Control
*   **Dimension Estimation:** Estimates the physical dimensions (width x height) of packages using camera calibration.
*   **Compliance Verification:** Detects specific visual markers, such as red "Fragile" stickers, to ensure proper handling.

### Analytics Dashboard
*   **Real-time Monitoring:** A web-based dashboard displays the live video feed with augmented reality overlays.
*   **Operational Stats:** Tracks key performance indicators including daily throughput, package counts, and peak activity hours.

## Technical Architecture

The system is built on a unified, modern technology stack:

*   **Backend:** Python (FastAPI)
*   **Frontend:** React (Vite) with Tailwind CSS
*   **AI/ML:** Ultralytics YOLOv8, EasyOCR, OpenCV
*   **Database:** SQLModel (SQLite/PostgreSQL)

## Installation

### Prerequisites
*   Python 3.10 or higher
*   Node.js 18 or higher
*   Webcam connected to the host machine

### Setup Steps

1.  **Backend Setup**
    Navigate to the project root and install Python dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```
    Start the backend server:
    ```bash
    python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
    ```

2.  **Frontend Setup**
    Open a new terminal window, navigate to the frontend directory, and install dependencies:
    ```bash
    cd frontend
    npm install
    ```
    Start the user interface:
    ```bash
    npm run dev
    ```

3.  **Usage**
    Open your web browser and navigate to http://localhost:5173 to access the dashboard.
