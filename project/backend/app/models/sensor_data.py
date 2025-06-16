from sqlalchemy import Column, Float, DateTime, Integer, String, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    container_id = Column(Integer, ForeignKey("containers.id"), nullable=False) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())
