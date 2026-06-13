# IoT-Enabled Smart Agriculture Monitoring Backend

This is a beginner-friendly backend for an **IoT-Enabled Smart Agriculture Monitoring System**. It supports virtual sensor simulation, threshold-based automation, alert generation, SQLite data logging, CSV export, and optional MQTT publishing.

## Features

- Accepts soil moisture, temperature, humidity, light intensity, and water level values.
- Automatically decides pump ON/OFF using threshold logic.
- Controls simulated fan and grow light status.
- Generates alerts for dry soil, high temperature, low water level, and low light.
- Saves readings in SQLite database.
- Exports sensor history as CSV.
- Includes Swagger API documentation at `/docs`.
- Works without real IoT hardware.

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Uvicorn
- Optional MQTT using `paho-mqtt`

## Folder Structure

```text
iot_smart_agriculture_backend/
├── app/
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── mqtt_client.py
│   ├── schemas.py
│   └── services.py
├── data/
├── docs/
│   └── API_ENDPOINTS.md
├── tests/
│   └── test_rules.py
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Setup

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create environment file

```bash
copy .env.example .env
```

On Mac/Linux:

```bash
cp .env.example .env
```

### 5. Run backend

```bash
python main.py
```

Open:

```text
http://127.0.0.1:8000/docs
```

## How to Test Without Hardware

Create a normal reading:

```bash
curl -X POST "http://127.0.0.1:8000/simulate?scenario=normal"
```

Create dry soil condition:

```bash
curl -X POST "http://127.0.0.1:8000/simulate?scenario=dry_soil"
```

Create high temperature condition:

```bash
curl -X POST "http://127.0.0.1:8000/simulate?scenario=high_temp"
```

Create low water level condition:

```bash
curl -X POST "http://127.0.0.1:8000/simulate?scenario=low_water"
```

View latest system status:

```bash
curl "http://127.0.0.1:8000/status"
```

## Add Manual Sensor Reading

```bash
curl -X POST "http://127.0.0.1:8000/readings" \
-H "Content-Type: application/json" \
-d "{\"soil_moisture\":25,\"temperature\":37,\"humidity\":45,\"light_intensity\":70,\"water_level\":80}"
```

Expected result:

- Pump ON because soil moisture is low.
- Fan ON because temperature is high.
- Alerts generated for low soil moisture and high temperature.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/readings` | Store a sensor reading |
| POST | `/simulate?scenario=dry_soil` | Generate virtual sensor data |
| GET | `/readings` | List latest readings |
| GET | `/status` | Latest system status |
| GET | `/export/csv` | Export data as CSV |

## Threshold Rules

| Parameter | Rule | Output |
|---|---|---|
| Soil moisture `< 35%` and water level `> 20%` | Dry soil | Pump ON |
| Soil moisture `< 35%` and water level `<= 20%` | Dry soil but no water | Pump OFF + alert |
| Temperature `> 35°C` | High temperature | Fan ON |
| Light intensity `< 25%` | Low light | Grow light ON |
| Water level `< 20%` | Low tank level | Alert |

## Optional MQTT

Set this in `.env`:

```env
ENABLE_MQTT=true
MQTT_BROKER=broker.hivemq.com
MQTT_PORT=1883
MQTT_TOPIC_DATA=farm/node1/data
MQTT_TOPIC_STATUS=farm/node1/status
```

The backend publishes readings to `farm/node1/data` and pump status to `farm/node1/status`.

## GitHub Proof-of-Work Suggestions

Commit in small steps:

```bash
git init
git add .
git commit -m "Initial FastAPI backend setup"
git commit -m "Add smart agriculture threshold automation"
git commit -m "Add virtual sensor simulation API"
git commit -m "Add SQLite logging and CSV export"
git commit -m "Add README and API documentation"
```

Recommended repo name:

```text
IoT-Smart-Agriculture-Monitoring-System
```

## Interview Explanation

I developed the backend for an IoT-enabled smart agriculture monitoring system. It receives sensor values such as soil moisture, temperature, humidity, light intensity, and water level. The backend processes the data using threshold rules, generates alerts, controls simulated devices like a water pump, fan, and grow light, stores readings in SQLite, and exposes APIs for dashboards or IoT devices.
