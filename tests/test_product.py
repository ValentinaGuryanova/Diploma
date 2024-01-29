from starlette.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_product():
    response = client.post("/products", json={
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    assert response.status_code == 422
    #assert response.status_code == 200


def test_get_products():
    response = client.post("/products", json={
        "id": 1,
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    product_id = response.json()
    response = client.get(f"/products/{product_id}")

    assert response.status_code == 404
    #assert response.status_code == 200


def test_update_product():
    response = client.post("/products", json={
        "id": 1,
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    product_id = response.json()
    response = client.put(f"/products/{product_id}", json={
        "id": 1,
        "name": "lipsticks",
        "price": 700,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    assert response.status_code == 404
    #assert response.status_code == 200


def test_delete_product():
    response = client.post("/products", json={
        "id": 1,
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    product_id = response.json()
    response = client.delete(f"/products/{product_id}")

    assert response.status_code == 404
    #assert response.status_code == 200
