import requests

header_data = {'T1': 'first_header', 'T2': 'second_header'}
response = requests.get('http://httpbin.org/get', headers=header_data)
print(response.text)