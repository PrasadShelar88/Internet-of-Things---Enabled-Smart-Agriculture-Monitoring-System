import json
from .config import settings


def publish_reading(reading: dict) -> None:
    """Optional MQTT publisher. Disabled by default for beginner-friendly local runs."""
    if not settings.enable_mqtt:
        return

    try:
        import paho.mqtt.client as mqtt
    except ImportError:
        print("MQTT enabled but paho-mqtt is not installed. Run: pip install paho-mqtt")
        return

    client = mqtt.Client()
    client.connect(settings.mqtt_broker, settings.mqtt_port, 60)
    client.publish(settings.mqtt_topic_data, json.dumps(reading))
    status = "PumpON" if reading.get("pump_on") else "PumpOFF"
    client.publish(settings.mqtt_topic_status, status)
    client.disconnect()
