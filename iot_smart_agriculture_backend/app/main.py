import csv
from io import StringIO
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import SensorReading
from .schemas import SensorReadingCreate, SensorReadingOut, SystemStatus
from .services import evaluate_controls, generate_virtual_reading
from .mqtt_client import publish_reading

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IoT-Enabled Smart Agriculture Monitoring Backend",
    description="Backend API for virtual smart agriculture sensor monitoring, automation, alerts, and data logging.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def serialize_reading(reading: SensorReading) -> SensorReadingOut:
    return SensorReadingOut(
        id=reading.id,
        created_at=reading.created_at,
        soil_moisture=reading.soil_moisture,
        temperature=reading.temperature,
        humidity=reading.humidity,
        light_intensity=reading.light_intensity,
        water_level=reading.water_level,
        pump_on=reading.pump_on,
        fan_on=reading.fan_on,
        grow_light_on=reading.grow_light_on,
        alerts=[a for a in reading.alerts.split("|") if a],
    )


@app.get("/")
def root():
    return {
        "message": "IoT Smart Agriculture Backend is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/readings", response_model=SensorReadingOut)
def create_reading(payload: SensorReadingCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    decision = evaluate_controls(data)
    reading = SensorReading(
        **data,
        pump_on=decision["pump_on"],
        fan_on=decision["fan_on"],
        grow_light_on=decision["grow_light_on"],
        alerts="|".join(decision["alerts"]),
    )
    db.add(reading)
    db.commit()
    db.refresh(reading)

    output = serialize_reading(reading)
    publish_reading(output.model_dump(mode="json"))
    return output


@app.post("/simulate", response_model=SensorReadingOut)
def simulate_reading(
    scenario: str = Query("normal", description="normal, dry_soil, high_temp, low_water, low_light"),
    db: Session = Depends(get_db),
):
    try:
        sample = generate_virtual_reading(scenario)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return create_reading(SensorReadingCreate(**sample), db)


@app.get("/readings", response_model=list[SensorReadingOut])
def list_readings(limit: int = Query(20, ge=1, le=500), db: Session = Depends(get_db)):
    readings = db.query(SensorReading).order_by(SensorReading.id.desc()).limit(limit).all()
    return [serialize_reading(r) for r in readings]


@app.get("/status", response_model=SystemStatus)
def system_status(db: Session = Depends(get_db)):
    latest = db.query(SensorReading).order_by(SensorReading.id.desc()).first()
    total = db.query(SensorReading).count()
    if latest is None:
        return SystemStatus(
            latest_reading=None,
            total_readings=0,
            pump_on=False,
            fan_on=False,
            grow_light_on=False,
            active_alerts=[],
        )
    latest_out = serialize_reading(latest)
    return SystemStatus(
        latest_reading=latest_out,
        total_readings=total,
        pump_on=latest.pump_on,
        fan_on=latest.fan_on,
        grow_light_on=latest.grow_light_on,
        active_alerts=latest_out.alerts,
    )


@app.get("/export/csv")
def export_csv(db: Session = Depends(get_db)):
    readings = db.query(SensorReading).order_by(SensorReading.id.asc()).all()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "id", "created_at", "soil_moisture", "temperature", "humidity",
        "light_intensity", "water_level", "pump_on", "fan_on", "grow_light_on", "alerts"
    ])
    for r in readings:
        writer.writerow([
            r.id, r.created_at.isoformat(), r.soil_moisture, r.temperature, r.humidity,
            r.light_intensity, r.water_level, r.pump_on, r.fan_on, r.grow_light_on, r.alerts
        ])
    output.seek(0)
    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=sensor_readings.csv"},
    )
