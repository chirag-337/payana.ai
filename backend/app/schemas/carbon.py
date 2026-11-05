from pydantic import BaseModel

class CarbonImpactReport(BaseModel):
    user_id: str
    total_trips_taken: int
    public_transit_km: float
    carbon_emissions_saved_kg: float
    time_reclaimed_minutes: int
    fuel_expenditure_saved_inr: float
    equivalent_trees_planted: float
    eco_rank: int

