import requests


def cycle_create(self):
    create_cycle_token = self.createtoken(self.createcycle_canonicalpath())
    cycle_id = create_cycle(self.project_id, self.version_id, self.cycle_name, create_cycle_token, self.access_key)
    return cycle_id

def create_cycle(project_id,version_id,cycle_name,token,access_key):
    url='https://prod-api.zephyr4jiracloud.com/connect/public/rest/api/1.0/cycle'
    headers = {
        'Authorization': 'JWT ' + token,
        'Content-Type': 'application/json',
        'zapiAccessKey': access_key
    }
    cycle = {
        'name': cycle_name,
        'projectId': project_id,
        'versionId': version_id,
    }
    raw_result = requests.post(url, headers=headers, json=cycle)
    import json
    print("Raw result ====", json.loads(raw_result.text)['id'])
    return json.loads(raw_result.text)['id']



