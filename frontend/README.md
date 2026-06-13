# IoT-Enabled Smart Agriculture Monitoring Frontend

This is the frontend dashboard for the **IoT-Enabled Smart Agriculture Monitoring System**. It connects to the FastAPI backend and displays live virtual sensor readings, actuator status, alerts, trends, manual sensor input, and CSV export.

## Features

- Backend health status
- Soil moisture, temperature, humidity, light intensity, and water level cards
- Pump, fan, and grow light ON/OFF status
- Active alert panel
- Sensor trend line chart
- Generate virtual readings using backend simulation scenarios
- Submit manual sensor readings
- Export logged sensor readings as CSV
- Auto-refresh dashboard every 5 seconds

## Tech Stack

- React
- Vite
- Recharts
- Lucide React icons
- FastAPI backend integration

## Required Backend

Start the backend first on:

```text
http://127.0.0.1:8000
```

The frontend uses these backend endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check backend status |
| GET | `/status` | Get latest system status |
| GET | `/readings?limit=30` | Get recent readings |
| POST | `/simulate?scenario=normal` | Generate virtual data |
| POST | `/readings` | Save manual sensor reading |
| GET | `/export/csv` | Download CSV logs |

## Setup

### 1. Install Node.js

Install Node.js LTS from the official website.

### 2. Install dependencies

```bash
npm install
```

### 3. Create environment file

Windows:

```bash
copy .env.example .env
```

Mac/Linux:

```bash
cp .env.example .env
```

Default `.env` value:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### 4. Run frontend

```bash
npm run dev
```

Open:

```text
http://127.0.0.1:5173
```

## How to Use

1. Start the backend.
2. Start this frontend.
3. Click **Generate Reading** to create simulated sensor data.
4. Select scenarios like `Dry Soil`, `High Temperature`, `Low Water`, or `Low Light` to test alerts.
5. Check actuator status:
   - Pump turns ON when soil is dry and water is available.
   - Fan turns ON when temperature is high.
   - Grow light turns ON when light intensity is low.
6. Use **Export CSV** to download logged readings.

## Good Screenshots for GitHub

- Dashboard home screen
- Normal reading output
- Dry soil alert with Pump ON
- Low water alert with Pump blocked/OFF
- High temperature alert with Fan ON
- Sensor trend graph
- Manual sensor reading form
- CSV export file

## Build for Production

```bash
npm run build
```

Preview production build:

```bash
npm run preview
```

## Project Folder Structure

```text
iot_smart_agriculture_frontend/
├── public/
├── src/
│   ├── api.js
│   ├── main.jsx
│   └── styles.css
├── .env.example
├── .gitignore
├── index.html
├── package.json
└── README.md
```
