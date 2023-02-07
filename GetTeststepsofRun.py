import json

import requests
import xmltodict


def get_teststeps(AlmBaseUrl,ALM_cookie,creationid):
    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/runs/{}/run-steps".format(AlmBaseUrl,creationid)
    payload = {}
    headers = {
        'Cookie': ALM_cookie,
    }
    response = requests.request("GET", url, headers=headers, data=payload,verify=False)
    assert (response.status_code == 200), "error:Message{} ".format(response.text)
    res = (response.content)
    runstepid = []
    my_dict = xmltodict.parse(res)
    json_data = my_dict
    for i in json_data['Entities']['Entity']:
        for j in i['Fields']['Field']:
            if j['@Name'] == 'id':
                runstepid.append(j['Value'])
    return runstepid
