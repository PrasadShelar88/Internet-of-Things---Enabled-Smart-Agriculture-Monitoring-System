# Frontend Notes

This frontend is designed for the FastAPI backend ZIP generated for the IoT Smart Agriculture project.

## Matching Backend Base URL

Default:

```text
http://127.0.0.1:8000
```

Change it in `.env` if your backend runs on another host or port.

## Simulation Scenarios

- normal
- dry_soil
- high_temp
- low_water
- low_light

## Common Errors

### Backend offline

Start backend first:

```bash
python main.py
```

### CORS error

The provided backend allows all origins. If you changed backend CORS settings, allow:

```text
http://127.0.0.1:5173
```
