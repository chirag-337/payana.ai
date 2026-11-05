from datetime import datetime
from typing import List, Dict, Any
from fastapi import APIRouter

router = APIRouter(prefix="/alerts", tags=["alerts"])

MOCK_ALERTS = [
    {
        "id": "ALT-01",
        "severity": "high",
        "title": "Severe Waterlogging near Ecospace (ORR)",
        "corridor": "Outer Ring Road",
        "impact": "Delays of 25-35 mins expected on routes 500D and 500A.",
        "created_at": datetime.utcnow().isoformat(),
    },
    {
        "id": "ALT-02",
        "severity": "medium",
        "title": "Namma Metro Phase 2B Construction - Airport Road",
        "corridor": "Hebbal - Yelahanka",
        "impact": "Lane constriction near Kogilu Cross; speed capped at 20 km/h.",
        "created_at": datetime.utcnow().isoformat(),
    },
    {
        "id": "ALT-03",
        "severity": "low",
        "title": "Extra Vajra Buses Deployed for Tech Park Peak",
        "corridor": "Whitefield ITPL",
        "impact": "Frequency augmented to every 4 minutes on 335E and V-335E.",
        "created_at": datetime.utcnow().isoformat(),
    },
]

@router.get("", response_model=List[Dict[str, Any]])
async def get_transit_alerts():
    """Retrieve active roadwork, weather, and transit disruption advisories."""
    return MOCK_ALERTS
