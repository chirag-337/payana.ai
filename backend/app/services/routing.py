from typing import List
from app.schemas.route import TransitRoute, TransitStop, PlanTripRequest, RouteRecommendation

# Bangalore transit routes catalog
_routes: List[TransitRoute] = [
    TransitRoute(
        route_id="R-500D",
        route_number="500D",
        source="Hebbal",
        destination="Central Silk Board",
        total_distance_km=29.4,
        estimated_duration_min=55,
        active_buses_count=18,
        frequency_minutes=5,
        stops=[
            TransitStop(stop_id="S1", name="Hebbal", latitude=13.0358, longitude=77.5970, sequence=1),
            TransitStop(stop_id="S2", name="Kalyan Nagar", latitude=13.0221, longitude=77.6403, sequence=2),
            TransitStop(stop_id="S3", name="Tin Factory", latitude=12.9972, longitude=77.6698, sequence=3),
            TransitStop(stop_id="S4", name="Marathahalli", latitude=12.9569, longitude=77.7011, sequence=4),
            TransitStop(stop_id="S5", name="Silk Board", latitude=12.9172, longitude=77.6228, sequence=5),
        ],
    ),
    TransitRoute(
        route_id="R-335E",
        route_number="335E",
        source="Kempegowda Bus Station (Majestic)",
        destination="Kadugodi / ITPL",
        total_distance_km=24.1,
        estimated_duration_min=48,
        active_buses_count=14,
        frequency_minutes=8,
        stops=[
            TransitStop(stop_id="S10", name="Majestic", latitude=12.9772, longitude=77.5713, sequence=1),
            TransitStop(stop_id="S11", name="Corporation", latitude=12.9667, longitude=77.5872, sequence=2),
            TransitStop(stop_id="S12", name="Domlur", latitude=12.9609, longitude=77.6387, sequence=3),
            TransitStop(stop_id="S13", name="ITPL Whitefield", latitude=12.9863, longitude=77.7300, sequence=4),
        ],
    ),
]

def get_routes() -> List[TransitRoute]:
    return _routes

def plan_journey(req: PlanTripRequest) -> List[RouteRecommendation]:
    return [
        RouteRecommendation(
            route_number="500D Express",
            departure_time="08:15 AM",
            arrival_time="09:05 AM",
            duration_min=50,
            co2_saved_kg=3.4,
            time_reclaimed_min=22,
            crowd_level="Medium (Seats available)",
            fare_inr=35.0,
        ),
        RouteRecommendation(
            route_number="V-500D Vajra AC",
            departure_time="08:22 AM",
            arrival_time="09:10 AM",
            duration_min=48,
            co2_saved_kg=3.2,
            time_reclaimed_min=25,
            crowd_level="Low (Air-conditioned)",
            fare_inr=55.0,
        ),
    ]

