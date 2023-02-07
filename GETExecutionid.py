import requests


def get_execution_id(access_key,token,project_id,cycle_id,version_id,issue_id):
    url ='https://prod-api.zephyr4jiracloud.com/connect/public/rest/api/1.0/execution'
    headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'application/json',
        'zapiAccessKey': access_key
    }
    Execution = {
            'cycleId': cycle_id,
            'projectId': project_id,
            'versionId': version_id ,
             'issueId': issue_id
    }
    import json;
    raw_result1 = requests.post(url, headers=headers, json=Execution)
    res = json.loads(raw_result1.text)
    print("res = ", res)
    execution_id =  res['id'] if 'id' in res else res['execution']['id']
    return execution_id

