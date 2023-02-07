import requests

jobid=aiq_1;
url = "https://api.eu-central-1.saucelabs.com/rest/v1/sshivaji/jobs/{}/assets/network.har".format(jobid)

payload={}
headers = {
  'Authorization': 'Basic c3NoaXZhamk6MmQwNWQzNDYtMGY3Mi00NGY1LTg3YTUtM2JlYmFiZGQ4NDRh'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
