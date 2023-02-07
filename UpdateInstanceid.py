import json

import requests
import xmltodict


def Update_TestInstance(AlmBaseUrl, ALM_cookie, status, value,ExecutionId):

    if status == "SUCCESS":
        status = "Passed"
    else:
        status = "Failed"

    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/test-instances/{}".format(AlmBaseUrl,value[2])
    ExecutionID_updated = str(ExecutionId)
    #print(ExecutionID_updated)

    payload = {"Fields": [{"Name": "user-05", "values": [{"value":ExecutionID_updated}]},{"Name": "status", "values": [{"value":status }]}]}
    #print(payload)
    headers = {
          'Content-Type': 'application/json',
          'Cookie':ALM_cookie,
    }
    response = requests.request("PUT", url, headers=headers, json=payload,verify=False)
    print(response.status_code)
    if response.status_code != 200:
        print('Test Instance Status Update => {}, response =>{} '.format(response.status_code,
                                                                                      response.text))

    res = (response.content)
    print(response)
    my_dict = xmltodict.parse(res)
    runid = None
    runstatus = None
    json_data = my_dict
    for run in json_data['Entity']['Fields']['Field']:
        if run['@Name'] == 'status':
            runstatus = run['Value']
    return runstatus


