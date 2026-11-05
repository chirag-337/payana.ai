from datetime import datetime
from typing import Dict, List, Optional
from app.schemas.bus import BusTelemetry

# In-memory store for real-time live telemetry
_live_buses: Dict[str, BusTelemetry] = {
    "BMTC-500D-01": BusTelemetry(
        bus_id="BMTC-500D-01",
        route_number="500D",
        latitude=12.9172,
        longitude=77.6228,
        speed_kmh=24.5,
        occupancy_percent=68,
        next_stop="Silk Board Junction",
        delay_minutes=4,
        status="on_route",
        timestamp=datetime.utcnow(),
    ),
    "BMTC-KIA9-04": BusTelemetry(
        bus_id="BMTC-KIA9-04",
        route_number="KIA-9",
        latitude=13.0358,
        longitude=77.5970,
        speed_kmh=48.0,
        occupancy_percent=42,
        next_stop="Hebbal Flyover",
        delay_minutes=1,
        status="on_route",
        timestamp=datetime.utcnow(),
    ),
    "BMTC-335E-12": BusTelemetry(
        bus_id="BMTC-335E-12",
        route_number="335E",
        latitude=12.9592,
        longitude=77.6974,
        speed_kmh=18.0,
        occupancy_percent=85,
        next_stop="ITPL Main Gate",
        delay_minutes=7,
        status="delayed",
        timestamp=datetime.utcnow(),
    ),
}

def get_all_buses() -> List[BusTelemetry]:
    return list(_live_buses.values())

def get_bus_by_id(bus_id: str) -> Optional[BusTelemetry]:
    return _live_buses.get(bus_id)

def upsert_bus_telemetry(telemetry: BusTelemetry) -> BusTelemetry:
    _live_buses[telemetry.bus_id] = telemetry
    return telemetry
