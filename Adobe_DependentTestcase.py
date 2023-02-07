import requests
import json

url = "https://adobe.autonomiq.ai/platform/v1/auth"

payload = json.dumps({
  "username": "adobeadmin",
  "password": "Adobeadmin@123"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRvYmVhZG1pbjpBZG9iZWFkbWluQDEyMw=='
}

response = requests.request("POST", url, headers=headers, data=payload)

j = json.loads(response.text)
token = j['token']
##print("FirstAPI",token)
##print("FirstAPI",token)

import requests

url = "https://adobe.autonomiq.ai/platform/v1/jobs/14/2/get_executions"

payload={}
headers = {
  'Authorization': 'Bearer {}'.format(token)
}

response = requests.request("GET", url, headers=headers, data=payload)
res = json.loads(response.text)

job = res['jobs'][0]
testcaseIds = []
executionStatus = []
testCaseName=[]
reportUrl = []
for task in job['etrs']['tasks']:
    testcaseIds.append(task['testcaseId'])
    executionStatus.append(task['executionStatus'])
    reportUrl.append(task['reportUrl'])


test_Report = dict(zip(testcaseIds, reportUrl))
print(test_Report)