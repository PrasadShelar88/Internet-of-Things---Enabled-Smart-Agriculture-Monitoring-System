# API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Use |
|---|---|---|
| GET | `/` | Check backend root |
| GET | `/health` | Health check |
| POST | `/readings` | Add real or manual sensor reading |
| POST | `/simulate?scenario=normal` | Generate virtual sensor reading |
| GET | `/readings?limit=20` | View latest readings |
| GET | `/status` | View latest actuator and alert status |
| GET | `/export/csv` | Download logged sensor data as CSV |

## Simulation scenarios

- `normal`
- `dry_soil`
- `high_temp`
- `low_water`
- `low_light`
