from pydantic import BaseModel
from datetime import datetime

class SensorDataBase(BaseModel):
    temperature: float
    humidity: float
    container_id: int 

class SensorDataCreate(SensorDataBase):
    pass

class SensorData(SensorDataBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True