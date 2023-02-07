import requests


def ALM_cookie_generation(AlmBaseUrl,clientid,secretid):
    url = "{}/qcbin/rest/oauth2/login".format(AlmBaseUrl)
    print("ALM base url",url)
    payload = {'clientId':clientid , 'secret':secretid}
    print("payload ALM",payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, json=payload,verify=False)
    assert (response.status_code == 200), "error:Failed to Generate cookies please enter correct clientid={} && secreteid={} ".format(clientid,secretid)
    cookie_str = ''
    for i in response.cookies:
        cookie_str += "{}={};".format(i.name, i.value)
    return cookie_str


