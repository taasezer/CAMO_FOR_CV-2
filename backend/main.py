from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import video, ai, database_api
from backend.database.database import init_db
import uvicorn

app = FastAPI(
    title="Ultimate Cargo Tracking System",
    description="AI-Powered Logistics Command Center",
    version="2.0.0"
)

# CORS Setup
origins = [
    "http://localhost:5173",  # Vite Frontend
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(video.router)
app.include_router(ai.router)
app.include_router(database_api.router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def root():
    return {"message": "System Operational", "status": "active"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
