import requests
import json
import xlsxwriter

RunIteration=2;
Date='2023-01-05';
workbook = xlsxwriter.Workbook('chart_bar.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

headings = ['TESTCASE NAME','SUCCESS','FAILURE']

##headings = ['Number', 'Batch 1', 'Batch 2']

url = "https://adobe.autonomiq.ai/platform/v1/auth"

payload = json.dumps({
  "username": "adobeadmin",
  "password": "Adobeadmin@123"
})
headers = {
  'Authorization': 'Basic YWRvYmVhZG1pbjpBZG9iZWFkbWluQDEyMw==',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

j = json.loads(response.text)
token = j['token']


TestExecutionName = []
FailureLength = []
SuccessLength = []
Failurecount = [0]
Successcount = [10]

Failurecount_ITR2 = []
Successcount_ITR2 = []


##value=[266,134,73,102,139,77,135,299,300,301,298,351,374,375,441,443,444]
##count=len(value);

##for i in value:

url = "https://adobe.autonomiq.ai/platform/testScriptExecutions/2/4/266/-1/0/executions"

payload={}
headers = {
		'Content-Type': 'application/json',
		'content-type': 'multipart/form-data',
		'Authorization': 'Bearer {}'.format(token)
}

response = requests.request("GET", url, headers=headers, data=payload)
L = json.loads(response.text)
ExecutionCount=L['tasks']

Executionvalue=53452;


def sum_lists(*args):
  return list(map(sum, zip(*args)))




failurecount = 0;
successcount = 0;
for i in ExecutionCount:
	if(Executionvalue==i['executionId']):
		print("inside loop")
		break;
	date1 = i['initiatedOn']
	date2 = date1.split('T')[0]
	if (Date == date2):
		if (i['executionStatus'] == "ERROR"):
			failurecount = failurecount + 1;
		if (i['executionStatus'] == "SUCCESS"):
			successcount = successcount + 1;
Failurecount_ITR2.append(failurecount)
Successcount_ITR2.append(successcount)

c = sum_lists(Failurecount_ITR2, Failurecount)
d = sum_lists(Successcount_ITR2, Successcount)

print(c);
print(d);