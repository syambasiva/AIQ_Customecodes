import json
import sys
import random
import requests
if __name__ == '__main__':
    url = "https://hooks.slack.com/services/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"
    message = ("Example")
    title = (f"Test Case Report")
    data = {
        "username": "AutonomIQ",
        "icon_emoji": ":exclamation:",
        "channel" : "#notification",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": "Link 1",
                        "value": "<http://foo.com|foo>",
                        "short": False
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)