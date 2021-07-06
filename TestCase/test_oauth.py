import requests
import json


def test_oauth_authorization():
    token_url = 'http://thetestingworldapi.com/token'
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'admin'}
    response = requests.post(token_url, data)
    json_response = response.json()
    print(json_response)
    # token_value = json_response['access_token']
    # auth = {'Authorization': 'Bearer {}'.format(token_value)}
    # api_url = 'http://thetestingworldapi.com/api/StDetails/1104'
    # response = requests.get(api_url, headers=auth)
    # json_response = response.json()
    # print(json_response)