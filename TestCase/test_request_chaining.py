import requests
import json


def test_add_new_student():
    global student_id
    api_url = 'http://thetestingworldapi.com/api/studentsDetails'
    with open('TestCase/create_student.json', 'r') as f:
        data = f.read()
    json_request = json.loads(data)
    response = requests.post(api_url, json_request)
    json_response = response.json()
    student_id = json_response['id']
    print(student_id)


def test_get_student_details():
    get_api_url = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(student_id)
    response = requests.get(get_api_url)
    json_response = response.json()
    print(json_response)
