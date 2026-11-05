from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.bus import BusTelemetry, BusTelemetryCreate
from app.services.telemetry import get_all_buses, get_bus_by_id, upsert_bus_telemetry

router = APIRouter(prefix="/buses", tags=["buses"])

@router.get("", response_model=List[BusTelemetry])
async def list_active_buses():
    """Retrieve all real-time tracking coordinates for active BMTC buses."""
    return get_all_buses()

@router.get("/{bus_id}", response_model=BusTelemetry)
async def get_bus_details(bus_id: str):
    """Get single bus live status, occupancy, and current speed."""
    bus = get_bus_by_id(bus_id)
    if not bus:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Bus {bus_id} not found")
    return bus

@router.post("/telemetry", response_model=BusTelemetry)
async def ingest_telemetry(payload: BusTelemetryCreate):
    """Ingest live GPS and occupancy telemetry from simulator or onboard IoT devices."""
    telemetry = BusTelemetry(**payload.model_dump())
    return upsert_bus_telemetry(telemetry)
