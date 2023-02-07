import requests


def Updating_step_Result(AlmBaseUrl,ALM_cookie, i,j,creationid):

    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/runs/{}/run-steps/{}".format(AlmBaseUrl,creationid,i)

    if j.get('status') == '0':
        val = 'Passed'
    else:
        val = 'Failed'
    payload = {"Fields": [{"Name": "status", "values": [{"value": val}]}]}


    headers = {
        'Content-Type': 'application/json',
        'Cookie': ALM_cookie
    }
    response = requests.request("PUT", url, headers=headers, json=payload,verify=False)
    assert (response.status_code == 200), "error:Message{} ".format(response.text)
