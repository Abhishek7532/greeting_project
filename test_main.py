from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_greet():
    response = client.get("/greet?name=Abhishek")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Abhishek!"}
