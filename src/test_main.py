import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Sample record identifier for testing
SAMPLE_RECORD_ID = "100"

# Test creating a valid record
def test_create_record_valid():
    new_record = [{
        "record_identifier": SAMPLE_RECORD_ID,
        "description": "Test record",
        "timestamp": "2024-07-13T12:00:00Z",
        "category": 1
    }]
    response = client.post("/records/", json=new_record)
    assert response.status_code == 200
    assert "status_code" in response.json()
    assert response.json()["status_code"] == 200

# Test creating a record with an invalid category type
def test_create_record_invalid_category():
    new_record = {
        "record_identifier": SAMPLE_RECORD_ID,
        "description": "Test record",
        "timestamp": "2024-07-13T12:00:00Z",
        "category": "invalid"  # Invalid category type
    }
    response = client.post("/", json=new_record)
    assert response.status_code != 200
    

# Test updating a valid record
def test_update_record_valid():
    updated_record = {
        "record_identifier": SAMPLE_RECORD_ID,
        "description": "Updated record",
        "timestamp": "2024-07-13T12:00:00Z",
        "category": 2
    }
    response = client.put(f"/{SAMPLE_RECORD_ID}", json=updated_record)
    assert response.status_code == 200
    assert "status_code" in response.json()
    assert response.json()["status_code"] == 200
    assert "Task updated successfully" in response.json()["message"]

# Test updating a non-existing record
def test_update_record_not_found():
    record_id = "non_existing_id"  # Non-existing record ID
    updated_record = {
        "record_identifier": record_id,
        "description": "Updated record",
        "timestamp": "2024-07-13T12:00:00Z",
        "category": 2
    }
    response = client.put(f"/{record_id}", json=updated_record)
    assert "detail" in response.json()
    assert "ID does not exist" in response.json()["detail"]