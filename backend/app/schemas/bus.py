from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from app.schemas.common import Coordinates

class BusTelemetry(BaseModel):
    bus_id: str
    route_number: str
    latitude: float
    longitude: float
    speed_kmh: float
    occupancy_percent: int
    next_stop: str
    delay_minutes: int
    status: str = "on_route"
    timestamp: datetime = datetime.utcnow()

class BusTelemetryCreate(BaseModel):
    bus_id: str
    route_number: str
    latitude: float
    longitude: float
    speed_kmh: float
    occupancy_percent: int
    next_stop: str
    delay_minutes: int

