import json
import jwt
import time
import hashlib
import requests


def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True


# USER
USER = 'admin'

# ACCESS KEY from navigation >> Tests >> API Keys
ACCESS_KEY = 'YzRmMWRlM2ItY2M1ZS0zMjcwLTk5MmUtYjQ0MjVhZDZjNzFlIDVmYmI2ZjJhY2JlYWQ1MDA2OTE3ZTJkOCBVU0VSX0RFRkFVTFRfTkFNRQ'

# ACCESS KEY from navigation >> Tests >> API Keys
SECRET_KEY = 'm2143WjBOMJMOFqq1wLQvCExbU55vPBDLv5GozZPzVE'

# JWT EXPIRE how long token been to be active? 3600 == 1 hour
JWT_EXPIRE = 3600

# BASE URL for Zephyr for Jira Cloud
BASE_URL = 'https://prod-api.zephyr4jiracloud.com/connect'

# CYCLE NAME FROM ZEPHYR
CYCLE_NAME = "sprint4"

PROJECT_NAME = "TestIQ"

IssueKey = "TIQ-128"

RELEASE_NAME = "Unscheduled";

Aiqteststatus= 2;

def post_result():
##### Fetching Release_Id and project_id ######

    RELATIVE_PATH = '/public/rest/api/1.0/zql/fields/values'
    CANONICAL_PATH = 'GET&'+RELATIVE_PATH+'&'
    payload_token = {
        'sub': USER,
        'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
        'iss': ACCESS_KEY,
        'exp': int(time.time()) + JWT_EXPIRE,
        'iat': int(time.time())
    }
    token = jwt.encode(payload_token, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')
    headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'text/plain',
        'zapiAccessKey': ACCESS_KEY
    }
    raw_result1 = requests.get(BASE_URL + RELATIVE_PATH, headers=headers)
    json_result = json.loads(raw_result1.text)
    print(json_result)
    versionid=json_result['fields']['fixVersion']
    projectid=json_result['fields']['project']
    for i in projectid:
        if i['name'] == PROJECT_NAME:
            PROJECT_ID=(i['id'])
    for i in versionid:
        if i['name'] == RELEASE_NAME:
            VERSION_ID=(i['id'])
    print(PROJECT_ID,VERSION_ID)

####FetchCycle_id##################

    RELATIVE_PATH = '/public/rest/api/1.0/cycles/search?versionId={}&projectId={}'.format(VERSION_ID, PROJECT_ID)

# CANONICAL PATH (Http Method & Relative Path & Query String)

    CANONICAL_PATH = 'GET&/public/rest/api/1.0/cycles/search&' + 'projectId=' + str(PROJECT_ID) + '&versionId=' + str(
    VERSION_ID)

# TOKEN HEADER: to generate jwt token
    payload_token = {
    'sub': USER,
    'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
    'iss': ACCESS_KEY,
    'exp': int(time.time()) + JWT_EXPIRE,
    'iat': int(time.time())
}

# GENERATE TOKEN
    token = jwt.encode(payload_token, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')

# REQUEST HEADER: to authenticate and authorize api
    headers = {
    'Authorization': 'JWT ' + token,
    'Content-Type': 'text/plain',
    'zapiAccessKey': ACCESS_KEY
}

    raw_result = requests.get(BASE_URL + RELATIVE_PATH, headers=headers)

    print("get cycle is", raw_result.text)

    test_cycle_ids = {}
    test_cycleidlist = []
    if is_json(raw_result.text):
         # JSON RESPONSE: convert response to JSON
        json_result = json.loads(raw_result.text)
        for json_val in json_result:
            print(json_val)
            if json_val['name'] == CYCLE_NAME:
                cycle_id = json_val['id']
                print(cycle_id)

    else:
        print(raw_result.text)

########## Fetch Execution_id and Issue_id ################
    RELATIVE_PATH = '/public/rest/api/1.0/executions/search/cycle/{}?versionId={}&projectId={}'.format(cycle_id, VERSION_ID, PROJECT_ID)

    CANONICAL_PATH = 'GET&/public/rest/api/1.0/executions/search/cycle/'+cycle_id+'&'+'projectId='+str(PROJECT_ID)+'&versionId=' + str(VERSION_ID)

    # TOKEN HEADER: to generate jwt token
    payload_token2 = {
                'sub': USER,
                'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
                'iss': ACCESS_KEY,
                'exp': int(time.time())+JWT_EXPIRE,
                'iat': int(time.time())
            }

    # GENERATE TOKEN
    token2 = jwt.encode(payload_token2, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')

    # REQUEST HEADER: to authenticate and authorize api
    headers2 = {
                'Authorization': 'JWT '+token2,
                'Content-Type': 'text/plain',
                'zapiAccessKey': ACCESS_KEY
            }
    result2 = requests.get(BASE_URL + RELATIVE_PATH, headers=headers2)

    test_details = {}
    test_cases_available = []
    if is_json(result2.text):
        # JSON RESPONSE: convert response to JSON
        json_result2 = json.loads(result2.text)
        print("fetch issue id",json_result2)
        #print("fetch list of all cycles",json_result2)
        for json_val in json_result2['searchObjectList']:
            if IssueKey == json_val['issueKey']:
                print(json_val['issueKey'])
                test_details['issueId'] = json_val['execution']['issueId']
                test_details['executionId'] = json_val['execution']['id']
        test_cases_available.append(test_details.copy())
            # PRINT RESPONSE: pretty print with 4 indent
        print("issueis \n",test_cases_available)
    else:
        print(result2.text)

    for i in test_cases_available:
        execution_id =i['executionId']
        issue_id = i['issueId']
#################################################################################
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
                "id": Aiqteststatus
            },
            "versionId": VERSION_ID
        }
        result2 = requests.put(BASE_URL + RELATIVE_PATH, headers=headers2, json=payload)
        print(result2.status_code)
        #print(result2.text)




if __name__ == "__main__":
    post_result()