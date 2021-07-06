import requests
import json

url = 'https://reqres.in/api/users/2'

with open('create_user.json', 'r') as f:
    data = f.read()
json_request_body = json.loads(data)
response = requests.put(url, json_request_body)
print(response.json())
print(response.status_code)
json_response_payload = response.json()
print(json_response_payload['updatedAt'])