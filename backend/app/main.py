"""Payana.ai FastAPI Backend Entrypoint."""
from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import (
    buses_router,
    routes_router,
    congestion_router,
    carbon_router,
    alerts_router,
    dashboard_router,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PayanaAI")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Payana.ai Transit Platform API...")
    logger.info("Initializing ML congestion model and bus telemetry registries...")
    yield
    logger.info("Shutting down Payana.ai API services...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Intelligent Central Transit Navigation Hub & ML-Powered Fleet Management API for Bengaluru.",
    lifespan=lifespan,
)

# CORS Middleware configured for local and deployed frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API Routers
app.include_router(buses_router, prefix=settings.API_PREFIX)
app.include_router(routes_router, prefix=settings.API_PREFIX)
app.include_router(congestion_router, prefix=settings.API_PREFIX)
app.include_router(carbon_router, prefix=settings.API_PREFIX)
app.include_router(alerts_router, prefix=settings.API_PREFIX)
app.include_router(dashboard_router, prefix=settings.API_PREFIX)

@app.get("/")
async def root():
    return {
        "project": "Payana.ai",
        "tagline": "Intelligent Bengaluru Transit Navigation Hub",
        "version": settings.VERSION,
        "docs_url": "/docs",
        "health": "healthy",
    }

