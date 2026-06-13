from app.services import evaluate_controls


def test_pump_turns_on_when_soil_is_dry_and_water_available():
    result = evaluate_controls({
        "soil_moisture": 20,
        "temperature": 28,
        "humidity": 60,
        "light_intensity": 70,
        "water_level": 80,
    })
    assert result["pump_on"] is True


def test_pump_blocked_when_water_is_low():
    result = evaluate_controls({
        "soil_moisture": 20,
        "temperature": 28,
        "humidity": 60,
        "light_intensity": 70,
        "water_level": 10,
    })
    assert result["pump_on"] is False
    assert any("PUMP_BLOCKED" in alert for alert in result["alerts"])
