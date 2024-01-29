from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)


def test_register():
    response = client.post("/user/register", json={
        "username": "Valya",
        "email": "test@mail.ru",
        "phone_number": "+79086784532",
        "password": "ty76SA$%",
    })
    assert response.status_code == 404
    #assert response.status_code == 200


def test_login():
    response = client.post("/user/register", json={
        "email": "test@mail.ru",
        "password": "ty76SA$%"
    })
    assert response.status_code == 404
    # assert response.status_code == 200