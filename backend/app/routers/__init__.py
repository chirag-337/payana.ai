from app.routers.buses import router as buses_router
from app.routers.routes import router as routes_router
from app.routers.congestion import router as congestion_router
from app.routers.carbon import router as carbon_router
from app.routers.alerts import router as alerts_router
from app.routers.dashboard import router as dashboard_router

__all__ = [
    "buses_router",
    "routes_router",
    "congestion_router",
    "carbon_router",
    "alerts_router",
    "dashboard_router",
]

