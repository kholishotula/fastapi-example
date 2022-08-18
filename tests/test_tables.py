import json
from fastapi.testclient import TestClient
from main import app

def test_crud_table_success():
    client = TestClient(app)
    response = client.post("/table/", json={
        "description": "T001",
        "status": 0
    })
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['data']['description'] == "T001"
    assert response_data['data']['status'] == False
    assert "id" in response_data['data']