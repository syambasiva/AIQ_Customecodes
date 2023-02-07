import requests

url = "https://api.imgur.com/3/account/me/images"

payload={}
headers = {
  'Authorization': 'Bearer a0bf5ad29f3c62e1ec5d613a0933d4e19b931e73'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
