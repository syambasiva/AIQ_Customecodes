import json

import requests

def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True

def FetchlistofTests(token,access_key,version_id,project_id,cycle_id):
    url = 'https://prod-api.zephyr4jiracloud.com/connect/public/rest/api/1.0/executions/search/cycle/{}?versionId={}&projectId={}'.format(cycle_id, version_id, project_id)

    headers = {
    'Authorization': 'JWT ' + token,
    'Content-Type': 'text/plain',
    'zapiAccessKey': access_key
     }

    result2 = requests.get(url,headers=headers)
    res = json.loads(result2.text)
    test_details = {}
    test_cases_available = []
    if is_json(result2.text):
        # JSON RESPONSE: convert response to JSON
        json_result2 = json.loads(result2.text)
        for json_val in json_result2['searchObjectList']:
            test_details['issueId'] = json_val['execution']['issueId']
            test_details['executionId'] = json_val['execution']['id']
            test_details['cyclename'] = json_val['execution']['cycleName']
            test_cases_available.append(test_details.copy())

    else:

     return test_cases_available

###################################################################################




    for i in test_cases_available:
        execution_id =i['executionId']
        issue_id = i['issueId']

        RELATIVE_PATH = '/public/rest/api/1.0/execution/{}?issueId={}&projectId=10006'.format(execution_id, issue_id)

        CANONICAL_PATH = 'PUT&/public/rest/api/1.0/execution/' + execution_id + '&' + 'issueId=' + str(
            issue_id) + '&projectId=' + str(PROJECT_ID)

        # TOKEN HEADER: to generate jwt token
        payload_token2 = {
            'sub': USER,
            'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
            'iss': ACCESS_KEY,
            'exp': int(time.time()) + JWT_EXPIRE,
            'iat': int(time.time())
        }

        # GENERATE TOKEN
        token2 = jwt.encode(payload_token2, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')

        # REQUEST HEADER: to authenticate and authorize api
        headers2 = {
            'Authorization': 'JWT ' + token2,
            'Content-Type': 'application/json',
            'zapiAccessKey': ACCESS_KEY
        }
        payload = {
            "cycleId": cycle_id,
            "id": execution_id,
            "issueId": issue_id,
            "projectId": PROJECT_ID,
            "status": {
                "id": "1"
            },
            "versionId": VERSION_ID
        }
        result2 = requests.put(BASE_URL + RELATIVE_PATH, headers=headers2, json=payload)
        print(result2)
        print(result2.text)