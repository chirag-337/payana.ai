from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/stats")
async def get_transit_kpis() -> Dict[str, Any]:
    """Summary overview statistics for Bengaluru central transit console."""
    return {
        "active_fleet_count": 6420,
        "on_time_performance_pct": 87.4,
        "daily_passengers_served": 3480000,
        "total_co2_offset_tonnes": 412.8,
        "average_city_speed_kmh": 22.4,
        "peak_congestion_index": 0.68,
        "primary_bottleneck": "Central Silk Board Junction",
    }

