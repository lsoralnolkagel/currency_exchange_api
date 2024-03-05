import pytest
from fastapi.testclient import TestClient
from CEA.main import app
from CEA.app.api.models.user import *
from CEA.app.api.models.currency import *

client = TestClient(app)


def test_models_currencytoexchange():
    data = {"currency_code_in": "EUR",
            "currency_code_out": "USD",
            "quantity": 2}
    currency_to_exchange = CurrencyToExchange(**data)
    assert currency_to_exchange.currency_code_in == "EUR"
    assert currency_to_exchange.currency_code_out == "USD"
    assert currency_to_exchange.quantity == 2


def test_models_currencyexchanged():
    data = {"currency_code_out": "EUR",
            "quantity": 12.5}
    currency_exchanged = CurrencyExchanged(**data)
    assert currency_exchanged.currency_code_out == "EUR"
    assert currency_exchanged.quantity == 12.5


def test_models_usertoregister():
    data = {"username": "testuser",
            "email": "testmail@mail.ru",
            "full_name": "Test User",
            "password": "TestPass09!"}
    user_to_register = UserToRegister(**data)
    assert user_to_register.username == "testuser"
    assert user_to_register.email == "testmail@mail.ru"
    assert user_to_register.full_name == "Test User"
    assert user_to_register.password == "TestPass09!"


def test_models_userindb():
    data = {"username": "testuser",
            "email": "testmail@mail.ru",
            "full_name": "Test User",
            "hashed_password": "password_to_hash"}
    user_in_db = UserInDB(**data)
    assert user_in_db.username == "testuser"
    assert user_in_db.email == "testmail@mail.ru"
    assert user_in_db.full_name == "Test User"


def test_models_usertologin():
    data = {"username": "testuser",
            "password": "TestPass09!"}
    user_to_login = UserToLogin(**data)
    assert user_to_login.username == "testuser"
    assert user_to_login.password == "TestPass09!"
