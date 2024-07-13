import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Sample record identifier for testing
SAMPLE_RECORD_ID = "1"

def test_create_record_valid():
    new_record = {
        "record_identifier": SAMPLE_RECORD_ID,
        "description": "Test record",
        "timestamp": "2024-07-13T12:00:00Z",
        "category": 1
    }
    response = client.post("/", json=new_record)
    assert response.status_code == 200
    assert "status_code" in response.json()
    assert response.json()["status_code"] == 200
    assert "Record created successfully" in response.json()["message"]

def test_create_record_invalid_category():
    new_record = {
        "record_identifier": SAMPLE_RECORD_ID,
        "description": "Test record",
        "timestamp": "2024-07-13T12:00:00Z",
        "category": "invalid"  # Invalid category type
    }
    response = client.post("/", json=new_record)
    assert response.status_code != 200
    

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

def test_delete_record_valid():
    response = client.delete(f"/delete/{SAMPLE_RECORD_ID}")
    assert response.status_code == 200
    assert "status_code" in response.json()
    assert response.json()["status_code"] == 200
    assert "Task deleted successfully" in response.json()["message"]

def test_delete_record_not_found():
    record_id = "non_existing_id"  # Non-existing record ID
    response = client.delete(f"/delete/{record_id}")
    assert "detail" in response.json()
    assert "ID does not exist" in response.json()["detail"]