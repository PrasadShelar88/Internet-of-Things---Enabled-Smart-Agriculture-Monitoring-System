# IoT-Enabled Smart Agriculture Monitoring System

## Project Overview

The **IoT-Enabled Smart Agriculture Monitoring System** is an IoT-based project designed to monitor important farm and greenhouse parameters such as **soil moisture, temperature, humidity, light intensity, and water level** in real time.

The system helps farmers and greenhouse owners make better irrigation decisions by checking sensor readings, generating alerts, and automatically controlling devices such as a **water pump, fan, or light** based on threshold values.

This project supports both:

* Hardware implementation using Arduino/ESP32 and sensors
* Virtual simulation using Python and dashboard-based sensor data

It is suitable for students who may not have access to real IoT hardware but still want to build a complete industry-oriented IoT project.

---

## Problem Statement

Traditional farming often depends on manual observation for watering crops and monitoring field conditions. This can lead to:

* Over-irrigation
* Under-irrigation
* Water wastage
* Poor crop health
* Delayed response to high temperature or low water level
* Lack of historical farm data

This project solves these problems by using IoT sensors and automation logic to monitor crop conditions continuously and take action at the right time.

---

## Objectives

The main objectives of this project are:

* Monitor soil moisture in real time
* Track temperature and humidity
* Monitor light intensity
* Check water tank level
* Generate alerts for abnormal conditions
* Automatically control irrigation pump
* Simulate IoT sensor readings without hardware
* Store sensor logs for analysis
* Provide a dashboard for real-time monitoring
* Build a GitHub-ready proof-of-work project

---

## Features

* Real-time soil moisture monitoring
* Temperature and humidity monitoring
* Light intensity monitoring
* Water level monitoring
* Automatic irrigation decision
* Pump ON/OFF simulation
* Fan/light control simulation
* Alert generation
* CSV data logging
* Dashboard visualization
* Virtual simulation mode
* Manual sensor input support
* REST API backend
* GitHub-ready project structure
* Beginner-friendly code and documentation

---

## IoT Concepts Used

This project demonstrates the following IoT concepts:

* Sensor data collection
* Microcontroller/simulation-based processing
* Threshold-based decision making
* Actuator control
* Real-time dashboard update
* Cloud/LAN communication concept
* Data logging
* Alert generation
* Automation logic
* Remote monitoring

---

## System Workflow

```text
Sensor Data
    ↓
ESP32 / Python Simulation
    ↓
Data Processing
    ↓
Threshold Checking
    ↓
Irrigation Decision
    ↓
Dashboard Update
    ↓
Alert Generation
    ↓
Pump / Fan / Light Control
```

---

## Architecture

```text
+---------------------+
| Sensors / Simulator |
|---------------------|
| Soil Moisture       |
| Temperature         |
| Humidity            |
| Light Intensity     |
| Water Level         |
+----------+----------+
           |
           v
+---------------------+
| Processing Unit     |
| ESP32 / Python API  |
+----------+----------+
           |
           v
+---------------------+
| Threshold Logic     |
| Alert Engine        |
| Irrigation Logic    |
+----------+----------+
           |
           v
+---------------------+
| Dashboard           |
| Logs                |
| Reports             |
+---------------------+
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLite
* CSV logging
* Uvicorn

### Frontend

* HTML / CSS / JavaScript or React
* Dashboard UI
* Chart visualization
* API integration

### Hardware / Simulation

* ESP32 or Arduino UNO
* Soil Moisture Sensor
* DHT11 / DHT22 Sensor
* LDR Sensor
* Water Level Sensor
* Relay Module
* Pump simulation
* Python-based virtual simulation

---

## Hardware Components

| Component            | Purpose                                  |
| -------------------- | ---------------------------------------- |
| ESP32 / Arduino UNO  | Reads sensor values and controls devices |
| Soil Moisture Sensor | Measures soil dryness/wetness            |
| DHT11 / DHT22        | Measures temperature and humidity        |
| LDR Sensor           | Measures light intensity                 |
| Water Level Sensor   | Detects available water level            |
| Relay Module         | Controls pump/fan/light                  |
| Water Pump           | Used for irrigation                      |
| Buzzer / LED         | Used for alerts                          |
| Power Supply         | Powers the circuit                       |

---

## Folder Structure

```text
IoT-Smart-Agriculture-Monitoring-System/
│
├── arduino_code/
│   └── smart_agriculture_esp32.ino
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── database.db
│   └── README.md
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   └── src/
│
├── python_simulation/
│   └── simulation.py
│
├── data/
│   └── sensor_logs.csv
│
├── outputs/
│   └── reports/
│
├── images/
│   └── dashboard_screenshot.png
│
├── circuit_diagram/
│   └── circuit.png
│
├── docs/
│   └── project_report.md
│
├── README.md
└── .gitignore
```

---

## Backend Setup

### Step 1: Open PowerShell

Go to the backend folder:

```powershell
cd "C:\Projects\IOT\Internet of Things - Enabled Smart Agriculture Monitoring System\iot_smart_agriculture_backend"
```

### Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

### Step 3: Activate Virtual Environment

```powershell
.\venv\Scripts\activate
```

### Step 4: Install Requirements

```powershell
pip install -r requirements.txt
```

### Step 5: Run Backend Server

```powershell
python -m uvicorn app.main:app --reload
```

### Step 6: Open API Docs

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Open a new PowerShell window.

### Step 1: Go to frontend folder

```powershell
cd "C:\Projects\IOT\Internet of Things - Enabled Smart Agriculture Monitoring System\iot_smart_agriculture_frontend"
```

### Step 2: Install frontend dependencies

```powershell
npm install
```

### Step 3: Run frontend

```powershell
npm run dev
```

### Step 4: Open frontend dashboard

```text
http://localhost:5173
```

---

## API Endpoints

| Method | Endpoint          | Description                     |
| ------ | ----------------- | ------------------------------- |
| GET    | `/`               | Backend health check            |
| GET    | `/latest`         | Get latest sensor reading       |
| GET    | `/readings`       | Get all sensor logs             |
| POST   | `/simulate`       | Generate virtual sensor reading |
| POST   | `/manual-reading` | Add manual sensor values        |
| POST   | `/control/pump`   | Control pump ON/OFF             |
| GET    | `/export/csv`     | Download CSV report             |
| DELETE | `/clear`          | Clear sensor logs               |

---

## Sample Sensor Data

```json
{
  "soil_moisture": 32,
  "temperature": 34.5,
  "humidity": 48,
  "light_intensity": 720,
  "water_level": 25,
  "pump_status": "ON",
  "alert": "LOW SOIL MOISTURE - PUMP TURNED ON"
}
```

---

## Threshold Logic

The project uses threshold-based automation.

Example logic:

```text
If soil moisture is below threshold:
    Turn pump ON
    Generate low moisture alert

If temperature is high:
    Generate high temperature alert
    Turn fan ON

If water level is low:
    Generate low water level alert

If light intensity is low:
    Turn light ON
```

---

## Virtual Simulation

If hardware is not available, this project supports virtual simulation.

Simulation scenarios include:

* Normal farm condition
* Dry soil condition
* Wet soil condition
* High temperature condition
* Low water level condition
* Low light condition
* Pump ON/OFF condition

This makes the project suitable for students who want to demonstrate IoT concepts without physical components.

---

## Dashboard Features

The dashboard displays:

* Soil moisture
* Temperature
* Humidity
* Light intensity
* Water level
* Pump status
* Fan/light status
* Alert message
* Sensor logs
* CSV export
* Manual reading input
* Simulation buttons

---

## Arduino / ESP32 Code Concept

The hardware version can use ESP32 with:

* Soil moisture sensor on analog pin
* DHT11/DHT22 on digital pin
* LDR on analog pin
* Water level sensor on analog pin
* Relay connected to pump

Basic logic:

```cpp
if (soilMoisture < threshold) {
  digitalWrite(relayPin, LOW);
  Serial.println("Pump ON");
} else {
  digitalWrite(relayPin, HIGH);
  Serial.println("Pump OFF");
}
```

---

## Applications

This project can be used in:

* Smart farming
* Greenhouse automation
* Polyhouse monitoring
* Nursery monitoring
* Irrigation automation
* Agriculture labs
* IoT learning projects
* Smart village projects

---

## Industry Relevance

Smart agriculture systems are used by:

* Farmers
* Agriculture companies
* Greenhouse owners
* Smart farming startups
* Irrigation teams
* Research labs
* AgriTech companies

Such systems help reduce water wastage, improve crop health, automate irrigation, and support data-driven farming decisions.

---

## Learning Outcomes

By completing this project, I learned:

* How IoT sensors collect environmental data
* How ESP32/Arduino can process sensor readings
* How Python can simulate IoT hardware
* How to build a FastAPI backend
* How to connect frontend dashboard with backend API
* How threshold-based automation works
* How to generate alerts
* How to log data into CSV/SQLite
* How to document and upload an IoT project on GitHub

---

## Future Improvements

Possible future improvements:

* Add MQTT support
* Add ThingSpeak integration
* Add Blynk mobile dashboard
* Add weather API integration
* Add automatic drip irrigation
* Add SMS/email alerts
* Add solar power support
* Add pH and EC sensors
* Add AI-based crop recommendation
* Add camera-based crop disease detection
* Add mobile app control

---

## Interview Preparation

### 1. Explain your project.

This is an IoT-based Smart Agriculture Monitoring System that monitors soil moisture, temperature, humidity, light intensity, and water level. Based on sensor readings, the system generates alerts and can automatically control a water pump, fan, or light. It helps farmers monitor crop conditions and reduce water wastage.

### 2. What problem does this project solve?

It solves the problem of manual field monitoring and inefficient irrigation. Farmers can know when soil is dry, when temperature is high, and when water level is low.

### 3. Which sensors are used?

The project can use a soil moisture sensor, DHT11/DHT22 temperature and humidity sensor, LDR sensor, and water level sensor.

### 4. Why did you use ESP32?

ESP32 is suitable because it has built-in Wi-Fi, good processing power, and can send data to dashboards or cloud platforms.

### 5. How does irrigation logic work?

The system checks soil moisture against a threshold. If soil moisture is low, the pump turns ON. If moisture is sufficient, the pump remains OFF.

### 6. How does this project use IoT?

It collects sensor data, processes it, sends it to a dashboard, generates alerts, and controls actuators remotely or automatically.

### 7. What is the output of this project?

The output includes sensor readings, alert messages, pump status, dashboard updates, and CSV logs.

### 8. Why is data logging useful?

Data logging helps analyze farm conditions over time and understand irrigation patterns.

### 9. What challenges did you face?

Challenges include setting correct thresholds, handling fluctuating sensor values, simulating hardware, and integrating the dashboard with backend APIs.

### 10. How can this project be improved?

It can be improved with mobile app alerts, weather API, automatic drip irrigation, AI crop recommendation, pH sensors, and cloud analytics.

---

## GitHub Repository Details

### Repository Name

```text
IoT-Smart-Agriculture-Monitoring-System
```

### Description

```text
An IoT-based smart agriculture monitoring system that tracks soil moisture, temperature, humidity, light intensity, and water level with automation, alerts, dashboard, and virtual simulation.
```

### GitHub Topics

```text
iot
smart-agriculture
esp32
arduino
fastapi
python
sensor-monitoring
agriculture-automation
irrigation-system
iot-dashboard
```

---

## Author

**Prasad Shelar**

---

## License

This project is created for educational and academic purposes. You can use and modify it for learning, college submissions, and portfolio building.

---

## Conclusion

The **IoT-Enabled Smart Agriculture Monitoring System** demonstrates how IoT can be used to improve agriculture through real-time monitoring, automation, alert generation, and data logging. It is beginner-friendly, simulation-ready, and suitable for GitHub portfolio and academic project submission.
