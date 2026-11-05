from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class CorridorCongestion(BaseModel):
    corridor_id: str
    name: str
    congestion_score: float  # 0.0 (free) to 1.0 (gridlock)
    level: str  # low, medium, heavy, severe
    avg_speed_kmh: float
    bottleneck_point: str
    predicted_trend: str  # improving, worsening, stable
    updated_at: datetime = datetime.utcnow()

class CongestionPredictionRequest(BaseModel):
    corridor_id: str
    hour_of_day: int
    day_of_week: int
    is_rainy: bool = False

