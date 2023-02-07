import requests
import json

url = "https://customersuccess.autonomiq.ai/platform/v1/auth"

payload = json.dumps({
  "username": "appuser",
  "password": "app@123!"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YXBwdXNlcjphcHBAMTIzIQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
