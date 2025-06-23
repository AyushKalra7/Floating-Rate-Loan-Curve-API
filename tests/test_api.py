import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def sample_payload():
    return {
        "maturity_date": "2026-01-01",
        "reference_rate": "SOFR",
        "rate_floor": 0.02,
        "rate_ceiling": 0.05,
        "rate_spread": 0.015
    }

def test_loan_rate_curve_valid(sample_payload):
    response = client.post("/loan-rate-curve", json=sample_payload)
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)
    assert len(result) > 0
    for item in result:
        assert "date" in item and "rate" in item
        assert sample_payload["rate_floor"] <= item["rate"] <= sample_payload["rate_ceiling"]

def test_invalid_reference_rate():
    payload = {
        "maturity_date": "2026-01-01",
        "reference_rate": "INVALID",
        "rate_floor": 0.02,
        "rate_ceiling": 0.05,
        "rate_spread": 0.015
    }
    response = client.post("/loan-rate-curve", json=payload)
    assert response.status_code == 200
    assert response.json() == []  # Invalid reference just returns nothing from DB