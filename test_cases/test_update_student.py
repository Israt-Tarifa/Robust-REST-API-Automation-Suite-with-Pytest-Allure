import requests
import pytest
from utils.helper_functions import create_student
from utils.config import BASE_URL


def test_create_student(login_data,student_payload):
    login_payload = login_data

    login_response = requests.post(url=f"{BASE_URL}/login",json=login_payload)
    token= login_response.json().get("authToken")

    headers={
        "Authorization": f"Bearer {token}"

    }

    response = requests.post(url=f"{BASE_URL}/api/student",json = student_payload, headers=headers)

    assert response.status_code in [200,201],\
        f"Student creation Failed, response: {response}"

    response_data = response.json()
    print("Response Data:", response_data)

    assert response_data["name"]== student_payload["name"]
    assert response_data["email"] == student_payload["email"]
    assert response_data["department"] == student_payload["department"]
    assert response_data["registrationId"] == student_payload["registrationId"]
    assert response_data["age"]== student_payload["age"]

def test_student_exist_in_list(login_data,student_payload):
    login_payload = login_data

    login_response = requests.post(url=f"{BASE_URL}/login", json=login_payload)
    token = login_response.json().get("authToken")
    headers = {
        "Authorization": f"Bearer {token}"

    }
    post_response = requests.post(url=f"{BASE_URL}/api/student", json=student_payload, headers=headers)

    assert post_response.status_code in [200, 201], \
        f"Student creation Failed, response: {post_response}"

    get_response = requests.get(f"{BASE_URL}/api/student", headers=headers,)
    assert get_response.status_code == 200, \
        f"get request Failed, response: {get_response}"

    students = get_response.json()
    emails = []
    for student in students:
        emails = student["email"]

    assert student_payload["email"] in emails,\
         f"Created student email is not found in student list"

    print(f"Student with email {student_payload['email']} found in the list")

def test_get_student_by_name(login_data,student_payload):
    login_payload = login_data

    login_response = requests.post(url=f"{BASE_URL}/login", json=login_payload)
    token = login_response.json().get("authToken")

    headers = {
        "Authorization": f"Bearer {token}"

    }
    post_response = requests.post(url=f"{BASE_URL}/api/student", json=student_payload, headers=headers)

    assert post_response.status_code in [200, 201], \
        f"Student creation Failed, response: {post_response}"

    name_to_search = student_payload["name"]
    response = requests.get(url=f"{BASE_URL}/api/student?name={name_to_search}",headers=headers)

    assert response.status_code == 200, \
        f"get by name Failed"
    data = response.json()

    assert len(data)>0, "No student returned for given name"

    for student in data:
        assert student["name"]==name_to_search,\
           f"Expected Name {name_to_search},got {student['name']}"
    print(f"Student with name '{name_to_search}' found successfully")

def test_get_student_by_registration_id(login_data,student_payload):
    payload = login_data

    login_response = requests.post(url=f"{BASE_URL}/login", json= payload)
    token = login_response.json().get("authToken")

    headers = {
        "Authorization": f"Bearer {token}"

    }
    post_response = create_student(BASE_URL,student_payload,headers)
    assert post_response.status_code in [200, 201], \
        f"Student creation Failed "

    created_student = post_response.json()
    registration_id = created_student["registrationId"]

    get_response = requests.get(url=f"{BASE_URL}/api/student/{registration_id}",headers=headers)
    student = get_response.json()


    assert student["registrationId"] == registration_id
    assert student["name"] == student_payload["name"]

    print(f"Student with registrationId {registration_id} validated successfully")

