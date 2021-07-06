import requests

param = {'p1': 'param1', 'p2': 'param2'}
response = requests.get('http://httpbin.org/get', params=param)
print(response.text)