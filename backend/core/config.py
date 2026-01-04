from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Ultimate Cargo Tracking System"
    DATABASE_URL: str = "sqlite:///./cargo.db"
    CAMERA_ID: int = 0

    class Config:
        env_file = ".env"

settings = Settings()
