from sqlalchemy.orm import Session
from app.models.sensor_data import SensorData
from app.schemas.sensor_data import SensorDataCreate

def create_sensor_data(db: Session, data: SensorDataCreate):
    db_data = SensorData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_sensor_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SensorData).offset(skip).limit(limit).all()