from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["project"] == "Payana.ai"
    assert data["health"] == "healthy"

def test_list_buses():
    response = client.get("/api/v1/buses")
    assert response.status_code == 200
    buses = response.json()
    assert isinstance(buses, list)
    assert len(buses) >= 1
    assert "route_number" in buses[0]

def test_list_routes():
    response = client.get("/api/v1/routes")
    assert response.status_code == 200
    routes = response.json()
    assert isinstance(routes, list)
    assert len(routes) >= 1

def test_congestion_corridors():
    response = client.get("/api/v1/congestion/corridors")
    assert response.status_code == 200
    corridors = response.json()
    assert isinstance(corridors, list)
    assert len(corridors) >= 1
