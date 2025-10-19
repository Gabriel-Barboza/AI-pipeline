from fastapi.testclient import TestClient
from src.api.app import app  

client = TestClient(app)

def test_read_root():

    response = client.get("/") 
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à API Otimizada!"}

def test_predict_invalid_missing_field():
    test_data_invalid = {
      "sepal_width": 3.5,
      "petal_length": 1.4,
      "petal_width": 0.2
    }
    
    response = client.post("/predict", json=test_data_invalid)
    assert response.status_code == 422
    response_json = response.json()
    assert response_json["detail"][0]["loc"] == ["body", "sepal_length"]
    assert response_json["detail"][0]["msg"] == "Field required"


def test_predict_invalid_wrong_type():

    test_data_invalid = {
      "sepal_length": "cinco", 
      "sepal_width": 3.5,
      "petal_length": 1.4,
      "petal_width": 0.2
    }
    
    response = client.post("/predict", json=test_data_invalid)
    
    assert response.status_code == 422
    response_json = response.json()
    assert response_json["detail"][0]["loc"] == ["body", "sepal_length"]
    assert "Input should be a valid number" in response_json["detail"][0]["msg"]