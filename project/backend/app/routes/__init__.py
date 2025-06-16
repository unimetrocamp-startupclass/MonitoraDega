from fastapi import APIRouter
from .sensor_data import router as sensor_router
from .container import router as container_router

router = APIRouter()

router.include_router(sensor_router, prefix="/api/sensor-data", tags=["sensor-data"])
router.include_router(container_router, prefix="/api/containers", tags=["containers"])