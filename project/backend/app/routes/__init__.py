from fastapi import APIRouter
from .sensor_data import router as sensor_router

router = APIRouter()

router.include_router(sensor_router, prefix="/api/sensor-data", tags=["sensor-data"])