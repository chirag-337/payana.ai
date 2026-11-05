from typing import Optional, Any
from pydantic import BaseModel

PROBLEM_BASE = "https://payana.ai/errors/"

class ApiResponse(BaseModel):
    success: bool = True
    message: str = "Operation completed successfully"
    data: Optional[Any] = None

class Coordinates(BaseModel):
    lat: float
    lng: float
