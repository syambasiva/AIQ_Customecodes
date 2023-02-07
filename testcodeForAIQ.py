import requests
import json

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

print(token)

import requests

url = "https://sonata.autonomiq.ai/platform/v1/jobs/60/2/get_executions"

payload={}
headers = {
  'Authorization': 'Bearer '+token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import requests

url = "https://sonata.autonomiq.ai/platform/v1/testexecutions/39697/getexecution"

payload={}
headers = {
  'Authorization': 'Bearer ' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

finalresp=json.loads(response.text)
print(finalresp)
resultData = finalresp['resultData']
IterationStatus = []
for i in resultData:
     resultData1 = (i['resultData'])
     ##print("Result of Iteration",resultData1)
     if resultData1:
          for j in resultData1["iterationResult"]:
              iterationResult = (resultData1["iterationResult"])
              print(iterationResult)
          for k in iterationResult:
            IterationStatus.append(k["is_success"])
            print(k["is_success"])
          print(IterationStatus)



