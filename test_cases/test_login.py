import pytest
import requests
from utils.config import BASE_URL

def test_get_token(login_data):
    login_payload = login_data

    response=requests.post(f"{BASE_URL}/login",json=login_payload)
    assert response.status_code ==200,\
    f"Login Failed.Response:{response}"
    token=response.json().get("authToken")
    print(f"Token:{token}")
    assert token is not None,"Auth token is not in response"






