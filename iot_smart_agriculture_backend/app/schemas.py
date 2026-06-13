from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class SensorReadingCreate(BaseModel):
    soil_moisture: float = Field(..., ge=0, le=100, description="Soil moisture percentage")
    temperature: float = Field(..., ge=-20, le=80, description="Temperature in Celsius")
    humidity: float = Field(..., ge=0, le=100, description="Humidity percentage")
    light_intensity: float = Field(..., ge=0, le=100, description="Light intensity percentage")
    water_level: float = Field(..., ge=0, le=100, description="Water tank level percentage")


class SensorReadingOut(SensorReadingCreate):
    id: int
    created_at: datetime
    pump_on: bool
    fan_on: bool
    grow_light_on: bool
    alerts: List[str]

    class Config:
        from_attributes = True


class SystemStatus(BaseModel):
    latest_reading: SensorReadingOut | None
    total_readings: int
    pump_on: bool
    fan_on: bool
    grow_light_on: bool
    active_alerts: List[str]
