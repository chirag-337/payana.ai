from typing import List
from fastapi import APIRouter
from app.schemas.route import TransitRoute, PlanTripRequest, RouteRecommendation
from app.services.routing import get_routes, plan_journey

router = APIRouter(prefix="/routes", tags=["routes"])

@router.get("", response_model=List[TransitRoute])
async def list_routes():
    """Retrieve catalog of Bengaluru bus routes and mapped stops."""
    return get_routes()

@router.post("/plan", response_model=List[RouteRecommendation])
async def plan_trip(request: PlanTripRequest):
    """Calculate fastest, lowest-emission transit journey with live delays factored in."""
    return plan_journey(request)
