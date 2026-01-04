from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class CargoBase(SQLModel):
    tracking_id: str = Field(index=True, unique=True)
    status: str = Field(default="pending") # pending, packed, shipped, delivered, issue
    customer_name: Optional[str] = None
    customer_address: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
class Cargo(CargoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    video_path: Optional[str] = None
    is_fragile: bool = False
    detected_dimensions: Optional[str] = None # e.g. "20x30x10"
    
class CargoCreate(CargoBase):
    pass

class CargoRead(CargoBase):
    id: int
    video_path: Optional[str]

# Audit Log for everything happening in the system
class SystemLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    event_type: str # detection, error, system
    description: str
    snapshot_path: Optional[str] = None
