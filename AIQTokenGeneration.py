import json

import requests


def create_token(username, password, platformurl):
    url = '{}/v1/auth'.format(platformurl)

    response = requests.post(url, headers={'Content-Type': 'application/json'},
                             json={'username':username, 'password':password,}, verify=False)

    if response.status_code != 200:
        print('Aiq token generation  API status code => {}, response =>{} '.format(response.status_code,response.text))

    return json.loads(response.text)['token']

