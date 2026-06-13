import random
from typing import Dict, List
from .config import settings


def evaluate_controls(payload: Dict[str, float]) -> Dict[str, object]:
    """Apply threshold rules and return actuator states plus alert messages."""
    alerts: List[str] = []

    pump_on = payload["soil_moisture"] < settings.soil_moisture_threshold and payload["water_level"] > settings.low_water_level_threshold
    fan_on = payload["temperature"] > settings.high_temperature_threshold
    grow_light_on = payload["light_intensity"] < settings.low_light_threshold

    if payload["soil_moisture"] < settings.soil_moisture_threshold:
        alerts.append("LOW_SOIL_MOISTURE: Soil is dry. Irrigation required.")
    if payload["temperature"] > settings.high_temperature_threshold:
        alerts.append("HIGH_TEMPERATURE: Temperature is above safe limit.")
    if payload["water_level"] < settings.low_water_level_threshold:
        alerts.append("LOW_WATER_LEVEL: Water tank level is low.")
    if payload["light_intensity"] < settings.low_light_threshold:
        alerts.append("LOW_LIGHT: Light intensity is low. Grow light recommended.")
    if payload["soil_moisture"] < settings.soil_moisture_threshold and payload["water_level"] <= settings.low_water_level_threshold:
        alerts.append("PUMP_BLOCKED: Soil is dry but pump cannot start because water level is low.")

    return {
        "pump_on": pump_on,
        "fan_on": fan_on,
        "grow_light_on": grow_light_on,
        "alerts": alerts,
    }


def generate_virtual_reading(scenario: str = "normal") -> Dict[str, float]:
    """Generate sample sensor values for virtual simulation/testing."""
    scenarios = {
        "normal": {
            "soil_moisture": random.uniform(45, 70),
            "temperature": random.uniform(24, 32),
            "humidity": random.uniform(45, 75),
            "light_intensity": random.uniform(40, 80),
            "water_level": random.uniform(50, 90),
        },
        "dry_soil": {
            "soil_moisture": random.uniform(10, 30),
            "temperature": random.uniform(28, 36),
            "humidity": random.uniform(30, 55),
            "light_intensity": random.uniform(45, 90),
            "water_level": random.uniform(45, 90),
        },
        "high_temp": {
            "soil_moisture": random.uniform(35, 60),
            "temperature": random.uniform(36, 45),
            "humidity": random.uniform(20, 45),
            "light_intensity": random.uniform(60, 95),
            "water_level": random.uniform(40, 90),
        },
        "low_water": {
            "soil_moisture": random.uniform(10, 35),
            "temperature": random.uniform(25, 36),
            "humidity": random.uniform(35, 70),
            "light_intensity": random.uniform(35, 85),
            "water_level": random.uniform(5, 18),
        },
        "low_light": {
            "soil_moisture": random.uniform(40, 75),
            "temperature": random.uniform(20, 30),
            "humidity": random.uniform(50, 85),
            "light_intensity": random.uniform(5, 22),
            "water_level": random.uniform(45, 95),
        },
    }
    if scenario not in scenarios:
        raise ValueError(f"Unknown scenario '{scenario}'. Use one of: {', '.join(scenarios)}")
    return {key: round(value, 2) for key, value in scenarios[scenario].items()}
