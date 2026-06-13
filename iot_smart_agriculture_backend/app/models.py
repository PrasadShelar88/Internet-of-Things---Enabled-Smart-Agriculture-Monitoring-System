from datetime import datetime
from sqlalchemy import Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    soil_moisture: Mapped[float] = mapped_column(Float)
    temperature: Mapped[float] = mapped_column(Float)
    humidity: Mapped[float] = mapped_column(Float)
    light_intensity: Mapped[float] = mapped_column(Float)
    water_level: Mapped[float] = mapped_column(Float)
    pump_on: Mapped[bool] = mapped_column(Boolean, default=False)
    fan_on: Mapped[bool] = mapped_column(Boolean, default=False)
    grow_light_on: Mapped[bool] = mapped_column(Boolean, default=False)
    alerts: Mapped[str] = mapped_column(String, default="")
