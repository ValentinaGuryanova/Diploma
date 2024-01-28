# from urllib import response
#
# from tests.conftest import client
#
#
# def test_register():
#     client.post("/user/register", json={
#         "username": "string",
#         "email": "string",
#         "phone_number": "string",
#         "password": "string",
#         "is_active": "bool",
#         "is_superuser": "bool",
#         "is_verified": "bool"
#     })
#     assert response.status_code == 201