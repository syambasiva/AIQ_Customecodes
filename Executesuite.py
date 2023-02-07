import json

import requests
def executesuite(gentoken):
    url = "https://engineering1.autonomiq.ai/platform/v1/testsuite/53/execute"
    payload = "{\"executionType\": \"smoke\", \"executionMode\": \"parallel\", \"isRemoteDriver\": false,\r\n\"remoteDriver\":\"\", \"platform\": \"Linux\", \"browserDetails\":[{\"browser\":\"Chrome\",\r\n\"browserVersion\":\"0.0\"}]}"
    headers = {
        'Authorization': 'Bearer ' + gentoken,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)['job_id']

