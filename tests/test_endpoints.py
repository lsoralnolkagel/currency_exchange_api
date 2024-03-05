import pytest
import requests
from fastapi.testclient import TestClient
from CEA.main import app

client = TestClient(app)


def test_currency_get_all_currency_list():
    response = client.get("/currency/list/")
    assert response.status_code == 200
    assert "USD" in response.text


def test_currency_get_exchange_courses():
    response_1 = client.get("/currency/exchange/?from_c=USD&to_c=EUR&amount=100")
    assert response_1.status_code == 200
    url = "https://api.apilayer.com/currency_data/convert?to=EUR&from=USD&amount=100"
    response_2 = requests.get(url)
    assert response_1.text in response_2.text


def test_users_register():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "TestPass0906"
    }
    response = client.post("/auth/register/", json=user_data)
    assert response.status_code == 200
    assert "token" in response.json()


def test_users_login():
    user_data = {
        "username": "testuser",
        "password": "TestPass0906"
    }
    response = client.post("/auth/login/", json=user_data)
    assert response.status_code == 200
    assert "token" in response.json()
