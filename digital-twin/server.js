import { createServer } from 'node:http';

const port = Number(process.env.TWIN_PORT || 4174);
const backendUrl = process.env.PAYANA_API_URL || 'http://127.0.0.1:8000';

// Bengaluru corridor waypoints for simulation
const busSimulationFleet = [
  {
    bus_id: 'BMTC-500D-01',
    route_number: '500D',
    corridor: 'Outer Ring Road (Hebbal -> Silk Board)',
    lat: 12.9172,
    lng: 77.6228,
    latDelta: 0.0008,
    lngDelta: 0.0004,
    speed: 28,
    occupancy: 65,
    nextStop: 'Silk Board Junction'
  },
  {
    bus_id: 'BMTC-335E-09',
    route_number: '335E',
    corridor: 'HAL Old Airport Road -> ITPL',
    lat: 12.9592,
    lng: 77.6974,
    latDelta: -0.0005,
    lngDelta: 0.0009,
    speed: 22,
    occupancy: 82,
    nextStop: 'Marathahalli Bridge'
  },
  {
    bus_id: 'BMTC-KIA9-03',
    route_number: 'KIA-9',
    corridor: 'Kempapura -> Airport',
    lat: 13.0358,
    lng: 77.5970,
    latDelta: 0.0012,
    lngDelta: 0.0002,
    speed: 52,
    occupancy: 40,
    nextStop: 'Hebbal Flyover'
  }
];

function tickSimulation() {
  for (const bus of busSimulationFleet) {
    bus.lat += (Math.random() - 0.48) * bus.latDelta;
    bus.lng += (Math.random() - 0.48) * bus.lngDelta;
    bus.speed = Math.max(10, Math.min(65, bus.speed + (Math.random() * 6 - 3)));
    bus.occupancy = Math.max(20, Math.min(95, bus.occupancy + (Math.random() > 0.6 ? 2 : -1)));
  }
}

// Tick every 3 seconds
setInterval(tickSimulation, 3000);

const server = createServer((req, res) => {
  // CORS Headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  if (req.url === '/twin/telemetry' || req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      status: 'active',
      city: 'Bengaluru',
      simulated_fleet_size: busSimulationFleet.length,
      buses: busSimulationFleet.map(b => ({
        ...b,
        speed_kmh: Math.round(b.speed),
        occupancy_pct: Math.round(b.occupancy),
        timestamp: new Date().toISOString()
      }))
    }, null, 2));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(port, () => {
  console.log(`[Payana Digital Twin] Transit simulator listening on http://localhost:${port}`);
  console.log(`[Payana Digital Twin] Streaming live Bengaluru bus telemetry...`);
});
