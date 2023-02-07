import os

import requests

def Attach_Report(AlmBaseUrl,ALM_cookie,creationid):
    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/runs/{}/attachments".format(AlmBaseUrl,creationid)
    filepath = os.path.abspath("report.html")
    files = open(filepath, "rb")
    headers = {
      'Content-Type': 'application/octet-stream',
       'Slug': 'report.html',
        'Cookie': ALM_cookie
    }
    response = requests.request("POST", url, headers=headers, data=files,verify=False)
    assert (response.status_code == 201), "error:Message{} ".format(response.text)


