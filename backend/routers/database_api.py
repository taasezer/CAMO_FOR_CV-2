from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from backend.database.database import get_session
from backend.models.models import Cargo, CargoCreate, CargoRead, SystemLog

router = APIRouter(
    prefix="/db",
    tags=["Database"]
)

@router.post("/cargo/", response_model=CargoRead)
def create_cargo(cargo: CargoCreate, session: Session = Depends(get_session)):
    db_cargo = Cargo.model_validate(cargo)
    session.add(db_cargo)
    session.commit()
    session.refresh(db_cargo)
    return db_cargo

@router.get("/cargo/", response_model=List[CargoRead])
def read_cargos(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    cargos = session.exec(select(Cargo).offset(offset).limit(limit)).all()
    return cargos

@router.get("/logs/", response_model=List[SystemLog])
def read_logs(limit: int = 50, session: Session = Depends(get_session)):
    logs = session.exec(select(SystemLog).order_by(SystemLog.timestamp.desc()).limit(limit)).all()
    return logs
