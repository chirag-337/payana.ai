from fastapi import APIRouter
from app.schemas.carbon import CarbonImpactReport

router = APIRouter(prefix="/carbon", tags=["carbon"])

@router.get("/metrics/{user_id}", response_model=CarbonImpactReport)
async def get_user_carbon_impact(user_id: str):
    """Retrieve personal and community commute ROI: CO2 emissions reduced and time saved."""
    return CarbonImpactReport(
        user_id=user_id,
        total_trips_taken=42,
        public_transit_km=368.5,
        carbon_emissions_saved_kg=84.2,
        time_reclaimed_minutes=310,
        fuel_expenditure_saved_inr=4250.0,
        equivalent_trees_planted=4.2,
        eco_rank=7,
    )
