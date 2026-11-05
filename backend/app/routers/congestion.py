from typing import List
from fastapi import APIRouter
from app.schemas.congestion import CorridorCongestion, CongestionPredictionRequest
from app.ml.registry import registry

router = APIRouter(prefix="/congestion", tags=["congestion"])

CORRIDORS = [
    {"id": "silk_board", "name": "Central Silk Board Junction", "bottleneck": "Hosur Road - Madiwala Link"},
    {"id": "outer_ring_road", "name": "Outer Ring Road (Marathahalli - Bellandur)", "bottleneck": "Iblur Junction"},
    {"id": "tin_factory", "name": "Tin Factory - KR Puram", "bottleneck": "Old Madras Road merge"},
    {"id": "hebbal_flyover", "name": "Hebbal Flyover (Airport Corridor)", "bottleneck": "Esteem Mall bottleneck"},
    {"id": "electronic_city_expressway", "name": "Electronic City Tollway", "bottleneck": "Bommanahalli descent"},
]

@router.get("/corridors", response_model=List[CorridorCongestion])
async def get_corridor_conditions():
    """Retrieve live congestion indexes and bottlenecks across primary Bengaluru arterial corridors."""
    model = registry.get_congestion_model()
    results = []
    import datetime
    now = datetime.datetime.now()
    
    for c in CORRIDORS:
        pred = model.predict(c["id"], now.hour, now.weekday())
        results.append(CorridorCongestion(
            corridor_id=c["id"],
            name=c["name"],
            congestion_score=pred["score"],
            level=pred["level"],
            avg_speed_kmh=pred["avg_speed_kmh"],
            bottleneck_point=c["bottleneck"],
            predicted_trend=pred["predicted_trend"],
            updated_at=now,
        ))
    return results

@router.post("/predict")
async def predict_congestion(req: CongestionPredictionRequest):
    """Run ML inference for forecasted corridor delay."""
    model = registry.get_congestion_model()
    return model.predict(req.corridor_id, req.hour_of_day, req.day_of_week, req.is_rainy)

