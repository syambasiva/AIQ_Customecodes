import requests
import json


username=aiq_1;
password=aiq_2;
testcaseid=aiq_3;
userid=aiq_4;
URL1=aiq_5;


##########################cloning testcase######################################################################
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



url = "{}/testCases/{}/{}/clone".format(URL1,userid,testcaseid)

print(url)

payload={}
headers = {'Authorization': 'Bearer ' + token
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response)
Uploadresponse=json.loads(response.text)

clonedtestcaseid=Uploadresponse['testCaseId']

print(clonedtestcaseid)
########################### Update Testcase ####################################################################








