const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
    ...options,
  });

  if (!response.ok) {
    let message = `Request failed with status ${response.status}`;
    try {
      const data = await response.json();
      message = data.detail || message;
    } catch {
      // Keep default message for non-JSON errors.
    }
    throw new Error(message);
  }

  const contentType = response.headers.get('content-type') || '';
  if (contentType.includes('application/json')) return response.json();
  return response;
}

export const api = {
  baseUrl: API_BASE_URL,
  health: () => request('/health'),
  status: () => request('/status'),
  readings: (limit = 20) => request(`/readings?limit=${limit}`),
  simulate: (scenario = 'normal') => request(`/simulate?scenario=${encodeURIComponent(scenario)}`, { method: 'POST' }),
  createReading: (payload) => request('/readings', { method: 'POST', body: JSON.stringify(payload) }),
  csvUrl: () => `${API_BASE_URL}/export/csv`,
};
