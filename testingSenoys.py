import csv
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

VERSION_ID=-1
print("versionis",type(VERSION_ID))
PROJECT_ID=10006
print("PROJECT_ID",type(PROJECT_ID))

cycleid='875f0567-dec9-4aa5-bb50-51e077c70c72'
PROJECT_NAME = "TestIQ"

IssueKey = "TIQ-128"

RELEASE_NAME = "Unscheduled";

Exporttype="CSV"

print("Exporttype",type(Exporttype))

RELATIVE_PATH = '/public/rest/api/1.0/cycle/875f0567-dec9-4aa5-bb50-51e077c70c72/export?projectId=10006&exportType=CSV&versionId=-1'

CANONICAL_PATH = 'GET&/public/rest/api/1.0/cycle/875f0567-dec9-4aa5-bb50-51e077c70c72/export&exportType=CSV&projectId=10006&versionId=-1'

print(CANONICAL_PATH)
print(RELATIVE_PATH)
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

url=BASE_URL + RELATIVE_PATH
print(url)
raw_result1 = requests.get(BASE_URL + RELATIVE_PATH, headers=headers)
print("raw result for test \n",raw_result1)
resp=raw_result1.text
print(resp)
print(type(resp))


############################################# Jobstatus ##################################################


RELATIVE_PATH = '/public/rest/api/1.0/jobprogress/{}'.format(resp)



CANONICAL_PATH = 'GET&/public/rest/api/1.0/jobprogress/{}&'.format(resp)
print(CANONICAL_PATH)

payload_token = {
        'sub': USER,
        'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
        'iss': ACCESS_KEY,
        'exp': int(time.time()) + JWT_EXPIRE,
        'iat': int(time.time())
}
token1 = jwt.encode(payload_token, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')

headers = {
        'Authorization': 'JWT ' + token1,
        'Content-Type': 'application/json',
        'zapiAccessKey': ACCESS_KEY
}


##print(BASE_URL + RELATIVE_PATH)
##time.sleep(10)
raw_result2 = requests.get(BASE_URL + RELATIVE_PATH, headers=headers)
##print("raw result for test \n",raw_result2.status_code)
resp1=raw_result2.text
##print(resp1)
j=json.loads(resp1)
downloadfilename=(j['summaryMessage'])
#print(downloadfilename)

########################################### download file ########################################################

RELATIVE_PATH = '/public/rest/api/1.0/cycle/export/download/{}'.format(downloadfilename)



CANONICAL_PATH = 'GET&/public/rest/api/1.0/cycle/export/download/{}&'.format(downloadfilename)
print(CANONICAL_PATH)

payload_token = {
        'sub': USER,
        'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
        'iss': ACCESS_KEY,
        'exp': int(time.time()) + JWT_EXPIRE,
        'iat': int(time.time())
}
token2 = jwt.encode(payload_token, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')

headers = {
        'Authorization': 'JWT ' + token2,
        'Content-Type': 'application/x-download',
        'zapiAccessKey': ACCESS_KEY
}


##print(BASE_URL + RELATIVE_PATH)
##time.sleep(10)
##raw_result2 = requests.get(BASE_URL + RELATIVE_PATH, headers=headers)
##print("raw result for test \n",raw_result2.status_code)
##resp3=raw_result2.text
##print(resp3)
##print(type(resp3))


####################################   Creating New steps  #####################################################################################################



RELATIVE_PATH = '/public/rest/api/1.0/teststep/10251?projectId=10006'

CANONICAL_PATH = 'POST&/public/rest/api/1.0/teststep/10251&projectId=10006'

payload_token = {
        'sub': USER,
        'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
        'iss': ACCESS_KEY,
        'exp': int(time.time()) + JWT_EXPIRE,
        'iat': int(time.time())
}
token = jwt.encode(payload_token, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')

payload= json.dumps({"step": "wait 5 sec", "data": "", "result": "", "customFieldValues": []})

headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'application/json',
        'zapiAccessKey': ACCESS_KEY
}

url=BASE_URL + RELATIVE_PATH
##print(url)
##raw_result1 = requests.post(BASE_URL + RELATIVE_PATH, headers=headers,data=payload)
##print("raw result for test \n",raw_result1.content)
##resp=raw_result1.text
##print(resp)

############################### Move Teststeps ############################################################



RELATIVE_PATH = '/public/rest/api/2.0/teststep/10251/ea0a3d80-3c9a-479c-aa9f-724941604ea6/move?projectId=10006'

CANONICAL_PATH = 'POST&/public/rest/api/2.0/teststep/10251/ea0a3d80-3c9a-479c-aa9f-724941604ea6/move&projectId=10006'

payload_token = {
        'sub': USER,
        'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
        'iss': ACCESS_KEY,
        'exp': int(time.time()) + JWT_EXPIRE,
        'iat': int(time.time())
}
token = jwt.encode(payload_token, SECRET_KEY, algorithm='HS256').strip().decode('utf-8')

payload= json.dumps({"after": "02d74904-a582-45cf-b97f-adf9bb019692"})

headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'application/json',
        'zapiAccessKey': ACCESS_KEY
}

url=BASE_URL + RELATIVE_PATH
##print(url)
##raw_result1 = requests.post(BASE_URL + RELATIVE_PATH, headers=headers,data=payload)
##print("raw result for test \n",raw_result1.content)
##resp=raw_result1.text


####################################### GET ALL TESTSTEPS ############################################################

RELATIVE_PATH = '/public/rest/api/1.0/teststep/10251?projectId=10006'

CANONICAL_PATH = 'GET&/public/rest/api/1.0/teststep/10251&projectId=10006'

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
        'Content-Type': 'application/json',
        'zapiAccessKey': ACCESS_KEY
}

url=BASE_URL + RELATIVE_PATH
##print(url)
raw_result1 = requests.get(BASE_URL + RELATIVE_PATH, headers=headers,data=payload)
print("raw result for test \n",raw_result1.content)
resp=raw_result1.text
print(resp)

####################################