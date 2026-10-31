from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_study_progress():
    response = client.get(
        "/study-progress",
        params={"earned_credits":85}
    )

    assert response.status_code == 200
    assert response.json()["remaining_credits"] ==35


def test_excess_credits():
    response = client.get(
        "/study-progress",
        params={"earned_credits":130}
    )

    assert response.status_code == 200
    assert response.json()["remaining_credits"]==0


def test_negative_credits():
    response = client.get(
        "/study-progress",
        params={"earned_credits":-20}
    )

    assert response.status_code == 422

def test_missing_credits():
    response = client.get("/study-progress")

    print(response.json())

    assert response.status_code == 422

def test_invalid_type():
    response = client.get(
        "/study-progress",
        params = {"earned_credits": "abc"}
    )

    print("Error response:", response.json())

    assert response.status_code == 422

def test_zero_credits():
    response = client.get(
        "/study-progress",
        params = {"earned_credits": 0}
    )

    assert response.status_code == 200
    assert response.json()["remaining_credits"] == 120

def test_exact_graduation_credits():
    response = client.get(
        "/study-progress",
        params={"earned_credits": 120}
    )

    assert response.status_code == 200
    assert response.json()["remaining_credits"] == 0
    