import os
os.environ["TESTING"] = "1"
import pytest
from fastapi.testclient import TestClient
from app.database import Base, engine
from app.main import app, seed_database

# Ensure database tables exist
Base.metadata.create_all(bind=engine)
seed_database()

client = TestClient(app)

def test_api_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "GLOFGuard" in data["service"]

def test_api_stations():
    response = client.get("/api/stations")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_api_risk_current():
    response = client.get("/api/risk/current")
    assert response.status_code == 200
    data = response.json()
    assert "final_fusion_score" in data
    assert "risk_class" in data
