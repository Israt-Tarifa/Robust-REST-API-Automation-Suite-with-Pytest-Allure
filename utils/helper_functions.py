import pytest
import requests

def create_student(base_url, payload, headers):
    response = requests.post(
        url=f"{base_url}/api/student",
        json=payload,
        headers=headers
    )
    return response