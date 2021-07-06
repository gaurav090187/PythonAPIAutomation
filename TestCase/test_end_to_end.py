import requests
import json


def test_add_new_student():
    api_url = 'http://thetestingworldapi.com/api/studentsDetails'
    with open('TestCase/create_student.json', 'r') as f:
        data = f.read()
    json_request = json.loads(data)
    response = requests.post(api_url, json_request)
    json_response = response.json()
    student_id = json_response['id']
    print(student_id)

    tech_api_url = 'http://thetestingworldapi.com/api/technicalskills'
    with open('TestCase/tech_details.json', 'r') as f:
        data = f.read()
    json_request = json.loads(data)
    json_request['id'] = student_id
    json_request['st_id'] = student_id
    response = requests.post(tech_api_url, json_request)
    json_response = response.json()
    print(json_response)

    address_api_url = 'http://thetestingworldapi.com/api/addresses'
    with open('TestCase/address.json', 'r') as f:
        data = f.read()
    json_request = json.loads(data)
    json_request['stId'] = student_id
    response = requests.post(address_api_url, json_request)
    json_response = response.json()
    print(json_response)

    final_api_url = 'http://thetestingworldapi.com/api/FinalStudentDetails/{}'.format(student_id)
    response = requests.get(final_api_url)
    json_response = response.json()
    print(json_response)