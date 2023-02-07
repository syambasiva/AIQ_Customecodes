import json

import requests
import xmltodict

def Updating_ActualResuult(AlmBaseUrl,ALM_cookie,i,creationid, j):
    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/runs/{}/run-steps/{}".format(AlmBaseUrl,creationid,i)
    payload={"Fields":[{"Name":"actual","values":[{"value": j.get('message')}]}]}

    headers = {
    'Content-Type': 'application/json',
    'Cookie': ALM_cookie
    }
    response = requests.request("PUT", url, headers=headers, json=payload,verify=False)
    assert (response.status_code == 200), "error:Message{} ".format(response.text)


