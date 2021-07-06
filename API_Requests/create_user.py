import requests
import json

url = 'https://reqres.in/api/users'

with open('create_user.json', 'r') as f:
    data = f.read()

json_request = json.loads(data)

response = requests.post(url, json_request)
print(response.status_code)
print(response.headers.get('Content-Type'))
# json_response_payload = response.json()
json_response_payload = json.loads(response.text)
print(json_response_payload['id'])