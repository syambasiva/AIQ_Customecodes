import requests
import json

TestcaseName='B_Testcase'
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

#print(token)


import requests

url = "https://sonata.autonomiq.ai/platform/v1/projects/249/testcases/upload"

payload={'json': '"{\\"sessionId\\":\\"\\"}"\'',
'json': '"{\\"accountId\\":23}"\''}
files=[
  ('casefile',('B_Testcase.xlsx',open('./B_Testcase.xlsx','rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')),
  ('artifacts',('Dependencies.py',open('./Dependencies.py','rb'),'application/octet-stream')),
  ('artifacts',('testingZephyr1.py',open('./testingZephyr1.py','rb'),'application/octet-stream')),
  ('artifacts',('GetExecutionStatus_withTestcaseName.py',open('./GetExecutionStatus_withTestcaseName.py','rb'),'application/octet-stream')),
  ('artifacts',('DeletingArtifacts_Testcase.py', open('DeletingArtifacts_Testcase.py', 'rb'), 'application/octet-stream'))
]
headers = {
'Authorization': 'Bearer ' + token
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

Uploadresponse=json.loads(response.text)

id=Uploadresponse['success']
testid=''
for i in id:
  testid=i['test_case_id']

print(testid)

