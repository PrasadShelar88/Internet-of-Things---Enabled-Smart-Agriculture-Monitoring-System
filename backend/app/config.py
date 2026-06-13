from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    app_name: str = "IoT Smart Agriculture Backend"
    database_url: str = "sqlite:///./data/agriculture.db"

    soil_moisture_threshold: float = 35.0
    high_temperature_threshold: float = 35.0
    low_water_level_threshold: float = 20.0
    low_light_threshold: float = 25.0

    enable_mqtt: bool = False
    mqtt_broker: str = "broker.hivemq.com"
    mqtt_port: int = 1883
    mqtt_topic_data: str = "farm/node1/data"
    mqtt_topic_status: str = "farm/node1/status"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
