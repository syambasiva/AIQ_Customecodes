import requests
import json


TestcaseID=2587;

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

url = "https://sonata.autonomiq.ai/platform/discovery/249/249/testData"

payload={}
headers = {
  'Authorization': 'Bearer ' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

response_0=response.text
response_1 = json.loads(response_0)
ArtifactId=[]
for i in response_1:
    for j in i['testCases']:
        if j == TestcaseID:
            ArtifactId.append(i['testDataId'])

print(ArtifactId)

for i in ArtifactId:
    import requests

    url = "https://sonata.autonomiq.ai/platform/testDatas/{}/deleteTestData".format(i)

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)

import requests
import json

url = "https://sonata.autonomiq.ai/platform/testCases/delete"

payload = json.dumps({
  "testcaseIds": [
TestcaseID
  ]
})
headers = {
  'Authorization': 'Bearer ' + token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
print(response.text)
