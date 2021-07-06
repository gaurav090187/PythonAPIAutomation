import requests
import jsonpath
import json
import pytest

url = 'https://reqres.in/api/users?page=2'


@pytest.mark.smoke
def test_fetch_user():
    response = requests.get(url)
    json_response = json.loads(response.text)
    data = jsonpath.jsonpath(json_response, 'data')
    data_size = len(data[0])
    print(data_size)
    for i in range(data_size):
        first_name = jsonpath.jsonpath(json_response, 'data[{}].first_name'.format(i))
        print(first_name[0])