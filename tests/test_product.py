# from starlette.testclient import TestClient
# from unittest.mock import Mock
# from main import app
# from products.models import Product
# from products.router import get_products
#
# client = TestClient(app)
#
#
# def test_add_products():
#     db_mock = Mock()
#     response = client.post("/products", json={
#         "id": 1,
#         "name": "lipstick",
#         "price": 500,
#         "created_at": "2024-01-21T00:00:00",
#         "updated_at": "2024-01-21T00:00:00",
#         "is_active": True
#     })
#
#
#     # Заглушаем метод query для возврата тестовых данных
#     db_mock.session.query().all.return_value = response
#
#     # Имитируем передачу заглушки объекта db в качестве зависимости
#     result = get_products(_=db_mock)
#
#     # Проверяем, что результат содержит ожидаемые данные
#     assert result["status"] == "success"
#     assert result["data"] == response
#     assert result["details"] is None
#
#
# async def test_get_products():
#     response = await client.post("/products", json={
#         "id": 1,
#         "name": "lipstick",
#         "price": 500,
#         "created_at": "2024-01-21T00:00:00",
#         "updated_at": "2024-01-21T00:00:00",
#         "is_active": True
#     })
#     product_id = response.json()["id"]
#     response = await client.get(f"/products/{product_id}")
#
#     assert response.status_code == 200
#     assert response.json()["status"] == "success"
#     assert len(response.json()["data"]) == 1
#
#
# async def test_update_product():
#     response = await client.post("/products", json={
#         "id": 1,
#         "name": "lipstick",
#         "price": 500,
#         "created_at": "2024-01-21T00:00:00",
#         "updated_at": "2024-01-21T00:00:00",
#         "is_active": True
#     })
#     product_id = response.json()["id"]
#     response = await client.put(f"/products/{product_id}", json={
#         "id": 1,
#         "name": "lipsticks",
#         "price": 800,
#         "created_at": "2024-01-21T00:00:00",
#         "updated_at": "2024-01-21T00:00:00",
#         "is_active": True
#     })
#     assert response.status_code == 200
#     assert response.json()["name"] == "new_name"
#     assert response.json()["price"] == "new_price"
#
#
# async def test_delete_product():
#     response = await client.post("/products", json={
#         "id": 1,
#         "name": "lipstick",
#         "price": 500,
#         "created_at": "2024-01-21T00:00:00",
#         "updated_at": "2024-01-21T00:00:00",
#         "is_active": True
#     })
#     product_id = response.json()["id"]
#     response = client.delete(f"/products/{product_id}")
#
#     assert response.status_code == 200
#     assert response.json()["status"] == "success"
