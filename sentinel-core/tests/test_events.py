import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "app": "SentinelCore"}

@pytest.mark.asyncio
async def test_ingest_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "service_name": "payment-api",
            "event_type": "CHARGE_FAILED",
            "severity": "ERROR",
            "payload": {"amount": 150, "currency": "TRY"},
            "user_id": "usr_102"
        }
        response = await ac.post("/api/v1/events/", json=payload)
    assert response.status_code == 202
    data = response.json()
    assert data["service_name"] == "payment-api"
    assert "id" in data