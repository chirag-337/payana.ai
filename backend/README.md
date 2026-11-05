# Payana.ai Backend API 🚌⚡

FastAPI-powered transit intelligence, route optimization, ML congestion prediction, and real-time fleet telemetry service for Bengaluru transit.

## Tech Stack
- **Framework:** FastAPI, Uvicorn
- **ML / Analytics:** Scikit-Learn, NumPy, Pandas
- **Data & Auth:** Supabase, PostgreSQL, JWT
- **Testing:** Pytest, HTTPX

## Setup Instructions

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the API development server:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. Open Swagger interactive documentation:
   `http://localhost:8000/docs`
