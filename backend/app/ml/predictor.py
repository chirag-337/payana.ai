"""ML congestion predictor for Bengaluru corridors."""
from typing import Dict, Any

class CongestionMLModel:
    def __init__(self):
        # Baseline corridor profiles
        self.corridor_weights = {
            "silk_board": 0.85,
            "outer_ring_road": 0.78,
            "tin_factory": 0.82,
            "hebbal_flyover": 0.74,
            "electronic_city_expressway": 0.52,
            "majestic_cbd": 0.68,
            "whitefield_itpl": 0.79,
        }

    def predict(self, corridor_id: str, hour: int, day_of_week: int, is_rainy: bool = False) -> Dict[str, Any]:
        base = self.corridor_weights.get(corridor_id.lower(), 0.50)
        
        # Rush hour penalty (8-11 AM, 5-8 PM)
        is_rush = (8 <= hour <= 11) or (17 <= hour <= 20)
        rush_multiplier = 1.35 if is_rush else 0.75
        
        # Weekend relief
        weekend_discount = 0.70 if day_of_week in (5, 6) else 1.0
        
        # Rain multiplier (Bangalore rain increases congestion significantly)
        rain_penalty = 1.25 if is_rainy else 1.0
        
        score = min(0.98, max(0.10, base * rush_multiplier * weekend_discount * rain_penalty))
        
        if score > 0.75:
            level = "severe"
            avg_speed = 12.0
            trend = "worsening" if is_rush else "improving"
        elif score > 0.55:
            level = "heavy"
            avg_speed = 18.5
            trend = "stable"
        elif score > 0.35:
            level = "medium"
            avg_speed = 28.0
            trend = "improving"
        else:
            level = "low"
            avg_speed = 42.0
            trend = "stable"
            
        return {
            "score": round(score, 2),
            "level": level,
            "avg_speed_kmh": avg_speed,
            "predicted_trend": trend,
        }

model_instance = CongestionMLModel()
