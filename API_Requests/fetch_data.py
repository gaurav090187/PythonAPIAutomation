import requests
import jsonpath
import json

url = 'https://reqres.in/api/users?page=2'

# response = requests.get(url)
# json_response = response.json()
# print(type(json_response))
# print('#' * 30)
# print(response.headers)
# print(response.status_code)
# assert response.status_code == 200, 'Failed to verify status code'
# print(response.headers.get('Date'))
# print(response.headers.get('Server'))
# print(response.cookies)
# print(response.encoding)
# print(response.elapsed)
# json_response = response.json()
# json_response = json.loads(response.text)
# print(json_response.get('total_pages'))
# total_pages = jsonpath.jsonpath(json_response, 'total_pages')
# print(total_pages[0])
# print(json_response['data'])
# for data in json_response['data']:
#     print(data['first_name'])
# data = jsonpath.jsonpath(json_response, 'data')
# data_size = len(data[0])
# print(data_size)
# for i in range(data_size):
#     first_name = jsonpath.jsonpath(json_response, 'data[{}].first_name'.format(i))
#     print(first_name[0])


with requests.get(url) as response:
    json_response = response.json()

print(json_response)