from conftest import client


def test_register():
    response = client.post("/auth/register", json={
                                                   "email": "pytest@example.com",
                                                   "password": "pytest_example",
                                                   "is_active": True,
                                                   "is_superuser": False,
                                                   "is_verified": False,
                                                   "username": "pytest_example"
                                                   })

    assert response.status_code == 201
