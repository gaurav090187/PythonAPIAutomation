import requests
import json


def test_create_new_student():
    api_url = 'http://thetestingworldapi.com/api/studentsDetails'
    with open('TestCase/create_student.json', 'r') as f:
        data = f.read()
    json_request = json.loads(data)
    response = requests.post(api_url, json_request)
    json_response = response.json()
    print(json_response['id'])
    return json_response['id']


def test_update_student():
    api_url = 'http://thetestingworldapi.com/api/studentsDetails/330477'
    with open('TestCase/create_student.json', 'r') as f:
        data = f.read()
    json_request = json.loads(data)
    response = requests.put(api_url, json_request)
    json_response = response.json()
    print(json_response)


def test_fetch_student():
    api_url = 'http://thetestingworldapi.com/api/studentsDetails/330477'
    response = requests.get(api_url)
    print(response.json())


def test_delete_student():
    api_url = 'http://thetestingworldapi.com/api/studentsDetails/330477'
    response = requests.delete(api_url)
    json_response = response.json()
    print(json_response)