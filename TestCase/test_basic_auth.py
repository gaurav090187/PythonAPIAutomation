import requests
from requests.auth import HTTPBasicAuth


def test_with_auth():
    api_url = 'https://api.github.com/user'
    response = requests.get(api_url, auth=HTTPBasicAuth('gaurav090187', 'Parrot@123456'))
    print(response.json())
