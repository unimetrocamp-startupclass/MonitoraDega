from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.schemas.sensor_data import SensorData, SensorDataCreate
from app.crud.sensor_data import create_sensor_data, get_sensor_data, get_sensor_data_by_container
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=SensorData)
def create_data(data: SensorDataCreate, db: Session = Depends(get_db)):
    return create_sensor_data(db=db, data=data)

@router.get("/", response_model=List[SensorData])
def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = get_sensor_data(db, skip=skip, limit=limit)
    return data

@router.get("/container/{container_id}", response_model=List[SensorData])
def read_data_by_container(container_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_sensor_data_by_container(db, container_id=container_id, skip=skip, limit=limit)