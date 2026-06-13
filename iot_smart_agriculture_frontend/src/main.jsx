import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Activity, AlertTriangle, Droplets, Fan, Gauge, Lightbulb, RefreshCw, Server, ThermometerSun, Waves } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';
import { api } from './api';
import './styles.css';

const scenarios = [
  { value: 'normal', label: 'Normal' },
  { value: 'dry_soil', label: 'Dry Soil' },
  { value: 'high_temp', label: 'High Temperature' },
  { value: 'low_water', label: 'Low Water' },
  { value: 'low_light', label: 'Low Light' },
];

const initialForm = {
  soil_moisture: 25,
  temperature: 32,
  humidity: 58,
  light_intensity: 70,
  water_level: 80,
};

function formatTime(value) {
  if (!value) return '-';
  return new Date(value).toLocaleString();
}

function StatusPill({ active, activeText, inactiveText }) {
  return <span className={`pill ${active ? 'pill-on' : 'pill-off'}`}>{active ? activeText : inactiveText}</span>;
}

function MetricCard({ title, value, suffix, icon, hint }) {
  return (
    <div className="metric-card">
      <div className="metric-header">
        <span>{title}</span>
        {icon}
      </div>
      <div className="metric-value">{value ?? '--'}<small>{suffix}</small></div>
      <p>{hint}</p>
    </div>
  );
}

function App() {
  const [health, setHealth] = useState('checking');
  const [status, setStatus] = useState(null);
  const [readings, setReadings] = useState([]);
  const [scenario, setScenario] = useState('normal');
  const [form, setForm] = useState(initialForm);
  const [loading, setLoading] = useState(false);
  const [autoRefresh, setAutoRefresh] = useState(true);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const latest = status?.latest_reading || readings[0] || null;

  const chartData = useMemo(() => {
    return [...readings].reverse().map((item) => ({
      time: new Date(item.created_at).toLocaleTimeString(),
      soil: item.soil_moisture,
      temp: item.temperature,
      humidity: item.humidity,
      light: item.light_intensity,
      water: item.water_level,
    }));
  }, [readings]);

  const loadDashboard = useCallback(async () => {
    setError('');
    try {
      const [healthData, statusData, readingsData] = await Promise.all([
        api.health(),
        api.status(),
        api.readings(30),
      ]);
      setHealth(healthData.status || 'healthy');
      setStatus(statusData);
      setReadings(readingsData);
    } catch (err) {
      setHealth('offline');
      setError(`${err.message}. Make sure the FastAPI backend is running on ${api.baseUrl}`);
    }
  }, []);

  useEffect(() => {
    loadDashboard();
  }, [loadDashboard]);

  useEffect(() => {
    if (!autoRefresh) return undefined;
    const id = setInterval(loadDashboard, 5000);
    return () => clearInterval(id);
  }, [autoRefresh, loadDashboard]);

  async function handleSimulate() {
    setLoading(true);
    setError('');
    setSuccess('');
    try {
      const created = await api.simulate(scenario);
      setSuccess(`Generated ${scenario.replace('_', ' ')} reading #${created.id}`);
      await loadDashboard();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleManualSubmit(event) {
    event.preventDefault();
    setLoading(true);
    setError('');
    setSuccess('');
    try {
      const payload = Object.fromEntries(Object.entries(form).map(([key, value]) => [key, Number(value)]));
      const created = await api.createReading(payload);
      setSuccess(`Manual reading saved. Pump is ${created.pump_on ? 'ON' : 'OFF'}.`);
      await loadDashboard();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  function updateForm(key, value) {
    setForm((current) => ({ ...current, [key]: value }));
  }

  return (
    <main>
      <section className="hero">
        <div>
          <p className="eyebrow">IoT Course Project Frontend</p>
          <h1>Smart Agriculture Monitoring Dashboard</h1>
          <p className="hero-text">
            Monitor virtual crop environment data, generate alerts, and track pump, fan, and grow light automation from the FastAPI backend.
          </p>
        </div>
        <div className="server-card">
          <Server size={28} />
          <span>Backend</span>
          <strong className={health === 'healthy' ? 'healthy' : 'offline'}>{health}</strong>
          <small>{api.baseUrl}</small>
        </div>
      </section>

      {error && <div className="notice error"><AlertTriangle size={18} /> {error}</div>}
      {success && <div className="notice success"><Activity size={18} /> {success}</div>}

      <section className="actions-panel">
        <div>
          <h2>Simulation Controls</h2>
          <p>Create virtual sensor data for normal, dry soil, high temperature, low water, or low light conditions.</p>
        </div>
        <div className="actions">
          <select value={scenario} onChange={(event) => setScenario(event.target.value)}>
            {scenarios.map((item) => <option key={item.value} value={item.value}>{item.label}</option>)}
          </select>
          <button onClick={handleSimulate} disabled={loading}>{loading ? 'Processing...' : 'Generate Reading'}</button>
          <button className="secondary" onClick={loadDashboard}><RefreshCw size={16} /> Refresh</button>
          <label className="checkbox"><input type="checkbox" checked={autoRefresh} onChange={(event) => setAutoRefresh(event.target.checked)} /> Auto refresh</label>
          <a className="download" href={api.csvUrl()} target="_blank" rel="noreferrer">Export CSV</a>
        </div>
      </section>

      <section className="grid metrics">
        <MetricCard title="Soil Moisture" value={latest?.soil_moisture} suffix="%" icon={<Droplets />} hint="Pump starts when soil is dry and water is available." />
        <MetricCard title="Temperature" value={latest?.temperature} suffix="°C" icon={<ThermometerSun />} hint="Fan turns ON when temperature crosses the threshold." />
        <MetricCard title="Humidity" value={latest?.humidity} suffix="%" icon={<Gauge />} hint="Useful for greenhouse and crop condition tracking." />
        <MetricCard title="Light Intensity" value={latest?.light_intensity} suffix="%" icon={<Lightbulb />} hint="Grow light turns ON when light is low." />
        <MetricCard title="Water Level" value={latest?.water_level} suffix="%" icon={<Waves />} hint="Low water blocks pump to avoid dry running." />
      </section>

      <section className="grid two-columns">
        <div className="panel">
          <h2>Actuator Status</h2>
          <div className="actuators">
            <div><Droplets /> Pump <StatusPill active={status?.pump_on} activeText="ON" inactiveText="OFF" /></div>
            <div><Fan /> Fan <StatusPill active={status?.fan_on} activeText="ON" inactiveText="OFF" /></div>
            <div><Lightbulb /> Grow Light <StatusPill active={status?.grow_light_on} activeText="ON" inactiveText="OFF" /></div>
          </div>
          <p className="muted">Total readings logged: <strong>{status?.total_readings ?? 0}</strong></p>
          <p className="muted">Latest update: <strong>{formatTime(latest?.created_at)}</strong></p>
        </div>

        <div className="panel">
          <h2>Active Alerts</h2>
          {status?.active_alerts?.length ? (
            <ul className="alerts">
              {status.active_alerts.map((alert) => <li key={alert}><AlertTriangle size={16} /> {alert}</li>)}
            </ul>
          ) : <p className="empty">No active alerts. Crop conditions are normal.</p>}
        </div>
      </section>

      <section className="panel chart-panel">
        <h2>Sensor Trends</h2>
        {chartData.length ? (
          <ResponsiveContainer width="100%" height={330}>
            <LineChart data={chartData} margin={{ top: 15, right: 25, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis domain={[0, 100]} />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="soil" name="Soil %" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="temp" name="Temp °C" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="humidity" name="Humidity %" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="light" name="Light %" strokeWidth={2} dot={false} />
              <Line type="monotone" dataKey="water" name="Water %" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        ) : <p className="empty">Generate a simulation reading to display graph data.</p>}
      </section>

      <section className="grid two-columns">
        <form className="panel" onSubmit={handleManualSubmit}>
          <h2>Manual Sensor Reading</h2>
          <div className="form-grid">
            {Object.entries(form).map(([key, value]) => (
              <label key={key}>
                {key.replaceAll('_', ' ')}
                <input type="number" min="0" max="100" step="0.1" value={value} onChange={(event) => updateForm(key, event.target.value)} />
              </label>
            ))}
          </div>
          <button type="submit" disabled={loading}>Save Manual Reading</button>
        </form>

        <div className="panel">
          <h2>Latest Readings</h2>
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>ID</th><th>Soil</th><th>Temp</th><th>Water</th><th>Pump</th>
                </tr>
              </thead>
              <tbody>
                {readings.slice(0, 8).map((row) => (
                  <tr key={row.id}>
                    <td>{row.id}</td>
                    <td>{row.soil_moisture}%</td>
                    <td>{row.temperature}°C</td>
                    <td>{row.water_level}%</td>
                    <td>{row.pump_on ? 'ON' : 'OFF'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
