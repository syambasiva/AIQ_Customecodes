import requests


def Download_report(platformurl,gentoken,report):
    url = "{}/v1/downloadFile?fileURL={}".format(platformurl,report)

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + gentoken
    }

    r = requests.get(url,headers=headers, data=payload,verify=False)
    assert (r.status_code == 200), "error:Message{} ".format(r.text)
    content = r.text
    with open('report.html', 'w') as f:
        f.write(content)
