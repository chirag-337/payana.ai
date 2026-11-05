# Payana.ai 🚌✨

<p align="center">
  <img src="https://img.shields.io/badge/SDG-11-Sustainable%20Cities%20and%20Communities-F99D26?style=for-the-badge" alt="SDG 11" />
  <img src="https://img.shields.io/badge/SDG-13-Climate%20Action-3F7E44?style=for-the-badge" alt="SDG 13" />
  <img src="https://img.shields.io/badge/Project-Payana.ai-0A84FF?style=for-the-badge" alt="Project Payana.ai" />
  <img src="https://img.shields.io/badge/Bengaluru-BMTC%20Transit%20Intelligence-FFB703?style=for-the-badge" alt="Transit Intelligence" />
</p>

Payana.ai is an intelligent central navigation hub and multimodal transit operations platform designed specifically for Bengaluru. It empowers commuters, tracks live BMTC bus telemetry in real time, forecasts corridor congestion using AI/ML, and quantifies environmental impact through carbon offset and "Time Reclaimed" metrics.

Built as a full-stack, hackathon-ready transit solution, it seamlessly unifies a Python FastAPI backend, a high-performance React + Vite operations dashboard, an IoT digital twin simulator, and a cross-platform Flutter commuter mobile application.

---

## Why this project matters

Bengaluru commuters lose hundreds of hours annually to traffic bottlenecks along key arteries such as the Outer Ring Road (ORR), Central Silk Board, Tin Factory, and Whitefield. A primary driver of congestion is the underutilization of public transit caused by unpredictable bus arrival times and lack of real-time visibility.

Payana.ai solves this by:
- **Tracking buses in real time:** Providing live telemetry, next-stop ETAs, and occupancy visibility so commuters never wait blindly.
- **Forecasting corridor bottlenecks:** Utilizing machine learning to detect traffic anomalies and reroute commuters before severe gridlock occurs.
- **Incentivizing sustainable mobility:** Tracking individualized and city-wide carbon emission reductions and commute ROI ("Time Reclaimed") against baseline private car travel.
- **Coordinating transit operations:** Equipping city operators with a centralized console to monitor fleet health, route adherence, and active transit alerts.

This directly advances **UN Sustainable Development Goal 11 (Sustainable Cities and Communities)** and **Goal 13 (Climate Action)** by boosting public transport adoption and slashing vehicular carbon emissions.

---

## Product overview

Payana.ai is composed of four integrated systems:

1. **Backend API (`backend/`)**: FastAPI microservice powered by Python, providing routing algorithms, scikit-learn congestion prediction models, Supabase data persistence, and telemetry ingestion.
2. **Web Operations Console (`app2/`)**: Modern React 19 + Vite dashboard with Tailwind CSS v4, Leaflet interactive mapping, Framer Motion transitions, and a feature-sliced architecture.
3. **Digital Twin Simulator (`digital-twin/`)**: Node.js streaming service that models and simulates live BMTC buses traveling along major Bengaluru transit corridors with dynamic speeds and passenger occupancies.
4. **Mobile App (`mobile/`)**: Flutter mobile application for smart commuters on Android and iOS, featuring trip planning, interactive maps, and personal carbon profile tracking.

---

## Key features

### 🗺️ Real-Time Navigation & Telemetry
- Live GPS tracking of BMTC buses (e.g. 500D, 335E, KIA-9) on interactive Leaflet maps.
- Dynamic route polylines, bus stop markers, and occupancy heat indicators.
- One-tap access to starred frequent journeys and multimodal connections.

### 🧠 Operational & Congestion Intelligence
- AI-assisted anomaly scoring and congestion prediction for key corridors (Silk Board, Tin Factory, Hebbal, ITPL).
- Traffic advisory alerts for roadwork, metro construction, and weather-induced waterlogging.
- Centralized fleet performance KPIs (active buses, on-time percentage, average speed).

### 🌱 Carbon Impact & Commute ROI Tracker
- Real-time calculator comparing transit emissions against private cab/car baselines.
- "Time Reclaimed" metric showing minutes saved from active driving stress.
- Community leaderboard rewarding eco-friendly commuters with badges and rankings.

### 🛰️ Live Infrastructure Simulation
- Digital twin telemetry generator simulating corridor bottlenecks and bus delays.
- Configurable simulation parameters for testing dispatch and rerouting logic under stress scenarios.

---

## Repository structure

```text
payana_ai/
├── README.md                 # Project architecture, setup, and overview
├── .gitignore                # Root gitignore for Python, Node, and Flutter
├── package.json              # Monorepo workspace configuration
├── app2/                     # Web Operations Console (React 19 + Vite)
│   ├── src/
│   │   ├── app/              # AppShell, Topbar, Sidebar, routing
│   │   ├── features/         # Feature-sliced modules (dashboard, map, routes, alerts, insights, carbon, auth)
│   │   ├── shared/           # Cross-cutting primitives (ui, lib, data, map)
│   │   └── styles/           # Tailwind CSS v4 styling & tokens
│   ├── package.json
│   ├── vite.config.ts
│   └── index.html
├── backend/                  # FastAPI Backend & ML Intelligence
│   ├── app/
│   │   ├── main.py           # FastAPI app & route mounting
│   │   ├── config.py         # Pydantic environment settings
│   │   ├── routers/          # Endpoints: buses, routes, congestion, carbon, alerts, dashboard
│   │   ├── schemas/          # Pydantic data schemas
│   │   ├── services/         # Routing and telemetry services
│   │   └── ml/               # Scikit-learn congestion prediction models
│   ├── requirements.txt      # Python dependencies
│   ├── pytest.ini
│   └── tests/                # Automated API test suite
├── digital-twin/             # BMTC Bus Telemetry Simulator
│   ├── server.js             # HTTP/WS telemetry streaming server
│   ├── dev.js
│   └── package.json
└── mobile/                   # Flutter Commuter Mobile Application
    ├── lib/                  # Dart source code (screens, widgets, providers)
    ├── pubspec.yaml          # Flutter dependencies
    └── README.md
```

---

## Architecture at a glance

```mermaid
flowchart LR
    A[BMTC GPS Telemetry / Digital Twin] --> B[FastAPI Backend Engine]
    B --> C[PostgreSQL / Supabase]
    B --> D[ML Congestion Predictor]
    B --> E[Web Operations Console (app2)]
    B --> F[Commuter Mobile App (mobile)]
    A --> G[Corridor Delay Analysis]
    G --> B
    E --> H[Route Optimization & Alerts]
    F --> H
    H --> I[Carbon Savings & Time Reclaimed]
```

---

## Tech stack

| Component | Technologies |
|---|---|
| **Web Operations Console (`app2`)** | React 19, Vite, TanStack Router, Tailwind CSS v4, Radix UI, React Leaflet, Lucide React, Framer Motion |
| **Backend API (`backend`)** | Python 3.11+, FastAPI, Uvicorn, Pydantic Settings, SQLAlchemy, Supabase SDK |
| **Machine Learning (`backend/app/ml`)** | Scikit-learn, NumPy, Pandas, Joblib |
| **Digital Twin Simulator (`digital-twin`)** | Node.js, Express, ES Modules |
| **Mobile App (`mobile`)** | Flutter, Dart, Riverpod, GoRouter, FlutterMap, LatLong2 |
| **Database & Auth** | PostgreSQL, Supabase, JWT |

---

## Getting started

### 1) Backend API

```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Swagger UI will be available at `http://localhost:8000/docs`.

### 2) Web Operations Console

```bash
cd app2
npm install
npm run dev
```
Open `http://localhost:8080` to access the live dashboard.

### 3) Digital Twin Bus Simulator

```bash
cd digital-twin
npm run api
```
Simulated bus telemetry stream is hosted at `http://localhost:4174/twin/telemetry`.

### 4) Commuter Mobile App

```bash
cd mobile
flutter pub get
flutter run
```

---

## Sustainable Development Goals (SDG) Impact

- **SDG 11.2 (Affordable and Sustainable Transport Systems):** Payana.ai expands access to predictable, clean public transportation by eliminating scheduling uncertainty and improving transit service transparency.
- **SDG 13.2 (Climate Change Mitigation):** By encouraging modal shift from private gasoline cars to BMTC electric and diesel fleets, each active user offsets over 80 kg of CO₂ per month.

---

## License

This project is licensed under the MIT License. Built with purpose for smarter, greener transit in Bengaluru.
