import requests
import json

testcaseid= aiq_1;

CYCLE_NAME = aiq_2;

PROJECT_NAME = aiq_3;

IssueKey = aiq_4;

RELEASE_NAME = aiq_5;

URL1=aiq_6;

username=aiq_7;

password=aiq_8;

projectid= aiq_9;




Testid_1=testcaseid.strip()





url = "{}/v1/auth".format(URL1)


payload = json.dumps({
  "username": username,
  "password": password
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic dGVzdGFkbWluOnRlc3RhZG1pbjEyMzQ='
}

response = requests.request("POST", url, headers=headers, data=payload)

resp=response.text

j = json.loads(resp)

token = j['token']



import requests
import json

url = "{}/v1/projects/{}/testcases/{}/updateSteps".format(URL1,projectid,Testid_1)



payload = json.dumps({
  "testSteps": [
    {
      "data": "http://example.com",
      "instr": "open website",
      "columnName": "",
      "expectedResults": "",
      "xpath": "",
      "stepId": ""
    },
    {
      "data": CYCLE_NAME,
      "instr": "save it as _CYCLE_NAME",
      "columnName": "",
      "expectedResults": "",
      "xpath": "",
      "stepId": ""
    },
    {
      "data": PROJECT_NAME,
      "instr": "save it as _PROJECT_NAME",
      "columnName": "",
      "expectedResults": "",
      "xpath": "",
      "stepId": ""
    },
    {
      "data": IssueKey,
      "instr": "save it as _IssueKey",
      "columnName": "",
      "expectedResults": "",
      "xpath": "",
      "stepId": ""
    },
    {
      "data": RELEASE_NAME,
      "instr": "save it as _RELEASE_NAME",
      "columnName": "",
      "expectedResults": "",
      "xpath": "",
      "stepId": ""
    },
    {
      "data": Testid_1,
      "instr": "save it as _Aiqtestid",
      "columnName": "",
      "expectedResults": "",
      "xpath": "",
      "stepId": ""
    },
    {
      "data": "",
      "instr": "Exec \"Dependencies.py\"",
      "columnName": "",
      "expectedResults": "",
      "xpath": "",
      "stepId": ""
    },
    {
      "data": "",
      "instr": "Exec \"testingZephyr1.py\"with ${_CYCLE_NAME},${_PROJECT_NAME},${_IssueKey},${_RELEASE_NAME},${_Aiqteststatus}, returning ${CSV_File1}",
      "columnName": "",
      "expectedResults": "",
      "xpath": "",
      "stepId": ""
    }
  ],
  "sessionId": "",
  "debugPoints": []
})
print(payload)
headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'

}
response = requests.request("POST", url, headers=headers, data=payload)
print(response)
print(response.status_code)
