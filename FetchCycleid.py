import json

import requests

def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True

def Fetch_cycleid(token,access_key,version_id,project_id):
    url = 'https://prod-api.zephyr4jiracloud.com/connect/public/rest/api/1.0/cycles/search?versionId={}&projectId={}'.format(version_id, project_id)

    headers = {
    'Authorization': 'JWT ' + token,
    'Content-Type': 'text/plain',
    'zapiAccessKey': access_key
     }

    raw_result = requests.get(url, headers=headers)
    res = json.loads(raw_result.text)
    cyclename=[]
    cycleid=[]
    for i in res:
        cyclename.append(i['name'])
        cycleid.append(i['id'])
    cycleName_cycleId = dict(zip(cyclename,cycleid))
    return cycleName_cycleId



