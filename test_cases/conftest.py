import pytest
import requests
from faker import Faker
from utils.config import BASE_URL,USERNAME,PASSWORD


@pytest.fixture()
def credentials():
    return {
        "username": USERNAME,
        "password": PASSWORD
    }
@pytest.fixture()
def auth_token(credentials):
    response = requests.post(url=f"{BASE_URL}/login", json=credentials)
    return response.json().get("authToken")

@pytest.fixture()
def headers(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}"
    }

@pytest.fixture
def login_data():
    return{
        "username":USERNAME,
        "password":PASSWORD
    }
    return BASE_URL,login_payload
@pytest.fixture
def student_schema():
    return{
    "name":str,
    "email":str,
    "department": str,
    "registrationId": int,
    "age": int
  }
fake=Faker()
@pytest.fixture
def student_payload():
    return{
        "name": fake.name(),
        "email": fake.unique.email(),
        "department": "CSE",
        "registrationId": fake.random_int(min=1000,max=9999),
        "age": fake.random_int(min=18,max=50)
    }