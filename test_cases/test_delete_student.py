import requests
from utils.helper_functions import create_student
from utils.config import BASE_URL

def test_delete_student_by_registration_id(headers, student_payload):
    #payload = login_data

    #login_response = requests.post(url=f"{BASE_URL}/login", json=payload)
    #token = login_response.json().get("authToken")
    #headers["Authorization"] = f"Bearer {token}"

    post_response = create_student(BASE_URL, student_payload, headers)


    if post_response.status_code != 201:
        print(f"\nError Details: {post_response.json()}")

    assert post_response.status_code in [200, 201]

    created_student = post_response.json()
    registration_id = created_student["registrationId"]

    delete_response = requests.delete(url=f"{BASE_URL}/api/student/{registration_id}", headers=headers)
    assert delete_response.status_code == 200, f"Delete failed! Response: {delete_response.text}"

    print(f"Student with registrationId {registration_id} deleted successfully.")

    get_response = requests.get(
        url=f"{BASE_URL}/api/student/{registration_id}",
        headers=headers
    )

    assert get_response.status_code in [400, 404], \
        "Deleted student still exists!"

    print(f"Verified student {registration_id} no longer exists")