import pytest
import requests
from utils.config import BASE_URL

def test_get_students(login_data,student_schema):
    login_payload = login_data

    login_response = requests.post(f"{BASE_URL}/login", json=login_payload)
    token = login_response.json().get("authToken")

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f"{BASE_URL}/api/student", headers=headers)
    assert response.status_code == 200, f"GET failed. Status: {response.status_code}"
    students = response.json()

    for student in students:
        for key,expected_type in student_schema.items():
            print(key, expected_type)
            assert key in student,f"key {key}  is missing in student"
            assert isinstance(student[key], expected_type),\
            f"key {key}  is {student[key]} != {expected_type},got {type(student[key])}"
