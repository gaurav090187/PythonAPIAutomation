import requests
import json
import pytest

url = 'https://reqres.in/api/users'


@pytest.fixture()
def start_exec():
    global data
    with open('TestCase/create_user.json', 'r') as file:
        data = file.read()


@pytest.mark.smoke
def test_create_new_user(start_exec):
    json_request = json.loads(data)
    response = requests.post(url, json_request)
    print(response.status_code)
    print(response.headers.get('Content-Type'))
    # json_response_payload = response.json()
    json_response_payload = json.loads(response.text)
    print(json_response_payload['id'])
    assert response.status_code == 201


@pytest.mark.sanity
def test_create_other_user(start_exec):
    json_request = json.loads(data)
    response = requests.post(url, json_request)
    print(response.status_code)
    print(response.headers.get('Content-Type'))
    # json_response_payload = response.json()
    json_response_payload = json.loads(response.text)
    print(json_response_payload['id'])