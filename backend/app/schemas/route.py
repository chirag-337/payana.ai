from typing import List, Optional
from pydantic import BaseModel
from app.schemas.common import Coordinates

class TransitStop(BaseModel):
    stop_id: str
    name: str
    latitude: float
    longitude: float
    sequence: int

class TransitRoute(BaseModel):
    route_id: str
    route_number: str
    source: str
    destination: str
    total_distance_km: float
    estimated_duration_min: int
    active_buses_count: int
    frequency_minutes: int
    stops: List[TransitStop] = []

class PlanTripRequest(BaseModel):
    origin: str
    destination: str
    prefer_ac: bool = False
    prioritize_speed: bool = True

class RouteRecommendation(BaseModel):
    route_number: str
    departure_time: str
    arrival_time: str
    duration_min: int
    co2_saved_kg: float
    time_reclaimed_min: int
    crowd_level: str
    fare_inr: float
