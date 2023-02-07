import requests
import json

TestcaseName="A_Testcase";
url = "https://sonata.autonomiq.ai/platform/v1/auth"

payload = json.dumps({
  "username": "testadmin",
  "password": "testadmin1234"
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

url = "https://sonata.autonomiq.ai/platform/v1/projects/249/testcases"

payload={}
headers = {
 'Authorization': 'Bearer ' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
finalresp=json.loads(response.text)
#print(finalresp)
TestcaseId=''
for i in finalresp:
    if i['testCaseName'] == TestcaseName:
        TestcaseId=i['testCaseId']


import requests

url = "https://sonata.autonomiq.ai/platform/testScriptExecutions/23/249/{}/-1/0/executions".format(TestcaseId)

payload={}
headers = {
  'Authorization': 'Bearer ' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

finalresp_1=json.loads(response.text)
#print(finalresp_1)
exeid=finalresp_1['tasks'][0]

#print(exeid['executionStatus'])
if exeid['executionStatus'] == "SUCCESS":
    print(1)
if exeid['executionStatus'] == "ERROR":
    print(2)


