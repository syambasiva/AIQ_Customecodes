def post_result():
    import json
    import json
    import jwt
    import time
    import hashlib
    import requests
    import requests
    import json
    # USER


    # CYCLE NAME FROM ZEPHYR

    # TestcaseId=aiq_1;

    CYCLE_NAME = 'sprint4';

    PROJECT_NAME = 'TestIQ';

    IssueKey = 'TIQ-128';

    RELEASE_NAME = 'Unscheduled';

    Aiqtestcasename = 'A_Testcase';

    URL1 = 'https://sonata.autonomiq.ai/platform';

    username = 'testadmin';


    password = 'testadmin1234';

    parent_projectid = 249;

    userAccount = 23;

    USER = 'admin';

    # ACCESS KEY from navigation >> Tests >> API Keys
    ACCESS_KEY = 'YzRmMWRlM2ItY2M1ZS0zMjcwLTk5MmUtYjQ0MjVhZDZjNzFlIDVmYmI2ZjJhY2JlYWQ1MDA2OTE3ZTJkOCBVU0VSX0RFRkFVTFRfTkFNRQ';

    # ACCESS KEY from navigation >> Tests >> API Keys
    SECRET_KEY = 'm2143WjBOMJMOFqq1wLQvCExbU55vPBDLv5GozZPzVE';

    # JWT EXPIRE how long token been to be active? 3600 == 1 hour
    JWT_EXPIRE = 3600

    # BASE URL for Zephyr for Jira Cloud
    BASE_URL = 'https://prod-api.zephyr4jiracloud.com/connect';

    ##TestcaseID = aiq_15;

    print( "CYCLE_NAME\n", CYCLE_NAME, "PROJECT_NAME\n", PROJECT_NAME, "IssueKey\n",
          IssueKey, "RELEASE_NAME\n", RELEASE_NAME, "Aiqtestcasename\n", Aiqtestcasename)

    def is_json(data):
        try:
            json.loads(data)
        except ValueError:
            return False
        return True
    #################        TOKEN  ##################################################################
    TestcaseName=Aiqtestcasename;
    url = "{}/v1/auth".format(URL1)
    print("username",username)
    payload = json.dumps({
         "username": username,
         "password": password
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic dGVzdGFkbWluOnRlc3RhZG1pbjEyMzQ='
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("response statuscode of token",response.status_code,"\n")
    resp=response.text

    j = json.loads(resp)

    aiq_token = j['token']
    print("token=",aiq_token,"\n")

####### FETCH TESTCASE ID ##############################################################################################

    url = "{}/v1/projects/{}/testcases".format(URL1,parent_projectid)

    payload={}
    headers = {
    'Authorization': 'Bearer ' + aiq_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print("response statuscode of TestcaseID of Testcase",response.status_code,"\n")
    #print(response.text)
    finalresp=json.loads(response.text)
    #print(finalresp)
    TestcaseId=''
    for i in finalresp:
        if i['testCaseName'] == TestcaseName:
            TestcaseId=i['testCaseId']

########################## GET STATUS ###########################################################################

    url = "{}/testScriptExecutions/{}/{}/{}/-1/0/executions".format(URL1,userAccount,parent_projectid,TestcaseId)

    payload={}
    headers = {
    'Authorization': 'Bearer ' + aiq_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print("response statuscode of Get AIQtestcase Execution Status",response.status_code,"\n")
    finalresp_1=json.loads(response.text)
    #print(finalresp_1)
    exeid=finalresp_1['tasks'][0]

    #print(exeid['executionStatus'])
    if exeid['executionStatus'] == "SUCCESS":
        Aiqteststatus=1
    if exeid['executionStatus'] == "ERROR":
        Aiqteststatus=2

    print("AIQ testcase status",Aiqteststatus,"\n")

##################          Fetching Release_Id and project_id   #############################################

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

############################    FetchCycle_id  #####################################################################

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

##########             Fetch Execution_id and Issue_id  ################################################################
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
        print(i)
        execution_id =i['executionId']
        issue_id = i['issueId']

#######################     UpdateStatusIn Zephyr #######################################################################
        RELATIVE_PATH = '/public/rest/api/1.0/execution/{}?issueId={}&projectId={}'.format(execution_id, issue_id,PROJECT_ID)


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
        print("response of Status update",result2)
        print("update status in zephyr",result2.status_code)
        #print(result2.text)



if __name__ == "__main__":
    post_result()