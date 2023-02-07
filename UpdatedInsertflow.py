import requests
import json


FromURL = aiq_1;

Fromusername=aiq_2;

FromPassword=aiq_3

FromProjectName=aiq_4

Fromflowname=aiq_5

ToURL=aiq_6

ToUsername=aiq_7

ToPassword=aiq_8

ToprojectName=aiq_9

# Base site Authentication and Userid
url = "{}/v1/auth".format(FromURL)

payload = json.dumps({
    "username": Fromusername,
    "password": FromPassword
})
headers = {
    'Authorization': 'Basic aW5kaHVtYXRoaTphaXFAMTIz',
    'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
resp11 = response.text
j = json.loads(resp11)
userid1 = j['userAccount']
token1 = j['token']
print("userid 1:")
print(userid1)
print("1.Authentication Status code \n",resp11,"\n",response.status_code)

# Base site Project details
projectname1 = FromProjectName

url = "{}/v1/getprojects".format(FromURL)

payload = {}
headers = {
    'Content-Type': 'application/json',
    'content-type': 'multipart/form-data',
    'Authorization': 'Bearer ' + token1,
}

response = requests.request("GET", url, headers=headers, data=payload)
resp12 = response.text
k = json.loads(resp12)
for i in k:
    if i['projectName'] == projectname1:
        projectid1 = (i['projectId'])
print("projectid1:")
print(projectid1)

print("2.project details and fetch projectid \n",resp12,"\n",response.status_code)

# Base site Flow Details
url = "{}/blocks/getAll/{}/{}".format(FromURL,userid1, projectid1)

payload = {}
headers = {
    'Authorization': 'Bearer ' + token1,
}

response = requests.request("GET", url, headers=headers, data=payload)
resp13 = response.text
l = json.loads(resp13)

for i in l:
    if (i['name']) == Fromflowname:
        flowsteps1 = (i)
print("Steps1:")
print(flowsteps1)

print("3.Fetching flow details \n",resp13,"\n",response.status_code)
# Required site Authentication and Userid
url = "{}/v1/auth".format(ToURL)

payload = json.dumps({
    "username": ToUsername,
    "password": ToPassword
})
headers = {
    'Authorization': 'Basic ZGVsbGFkbWluOmRlbGxhZG1pbjEyMzQ=',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
resp21 = response.text
m = json.loads(resp21)
userid2 = m['userAccount']
token2 = m['token']
print("userid 2:")
print(userid2)

print("4. Authentication of To Instance \n",resp21,"\n",response.status_code)
# Required Project Details
projectname2 = ToprojectName

url = "{}/v1/getprojects".format(ToURL)

payload = {}
headers = {
    'Content-Type': 'application/json',
    'content-type': 'multipart/form-data',
    'Authorization': 'Bearer ' + token2,
}

response = requests.request("GET", url, headers=headers, data=payload)
resp22 = response.text
n = json.loads(resp22)

for i in n:
    if i['projectName'] == projectname2:
        projectid2 = (i['projectId'])
print("projectid2:")
print(projectid2)

print("5. fetch project details \n",resp22,"\n",response.status_code)

# edit Json
insert_object = json.dumps(flowsteps1)
insert_object = json.loads(insert_object)
insert_object["accountId"] = userid2
insert_object["projectId"] = projectid2

print(insert_object)
print(type(insert_object))
# Required site Flow Details
url = "{}/blocks/getAll/{}/{}".format(ToURL,userid2, projectid2)

payload = {}
headers = {
    'Authorization': 'Bearer ' + token2,
}

response = requests.request("GET", url, headers=headers, data=payload)
resp23 = response.text
o = json.loads(resp23)

print("6. Fetching the flow details of to URL",resp23,"\n",response.status_code)

for i in o:
    if (i['name']) == Fromflowname:
        flowsteps2 = (i)
        print("Steps2:")
        print(flowsteps2)

        # edit Json
        json_object2 = json.dumps(flowsteps2)
        json_object2 = json.loads(json_object2)
        accId = json_object2["accountId"]
        projId = json_object2["projectId"]
        flowname = json_object2["name"]
        delete_object = {"account_id": accId, "project_id": projId, "name": flowname}
        print(type(delete_object))
        # delete exisiting
        url = "{}/v1/blocks/delete".format(ToURL)

        payload = json.dumps(delete_object)
        headers = {
            'Authorization': 'Bearer ' + token2,
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print("7. deleting if flow exists",response.text,"\n",response.status_code)

# Final insertion
url = "{}/blocks/insert".format(ToURL)

payload = json.dumps(insert_object)
headers = {
    'Authorization': 'Bearer ' + token2,
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("8. insertion of flow in To instance",response.text,"\n",response.status_code)