#params=aiq_1;
import ast

params="anonymousBody=Database.executeBatch(new CfltBatchCreateRenewalOppty());"

import json
import requests
url = "https://confluent--uat.my.salesforce.com/services/oauth2/token?username=sahal.mohamed@brillio.com.uat&password=test123%23&grant_type=password&client_id=3MVG9Ccwq.TeycMZqNopfSpQDzzUlRREavlR03uAoSq9EsZJQC4NJ7EqOS6Fy0ZtBcx5ddyjrAcbU3V.fqo0o&client_secret=2EDA257171B36B09DA4FE5F28B25DCF805744584ADA9515439C394360876C3B0"

payload={}
headers = {
  'Cookie': 'BrowserId=Z6o69ogLEeythDMoSBXnCw; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}
response = requests.request("POST", url, headers=headers, data=payload)
j = json.loads(response.text)
token = j['access_token']

url = "https://confluent--uat.my.salesforce.com/services/data/v54.0/tooling/executeAnonymous/?{}".format(params)
payload={}
headers = {
    'Authorization': "Bearer {}".format(token),
    'Cookie': 'BrowserId=Z6o69ogLEeythDMoSBXnCw; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}
response = requests.request("GET", url, headers=headers, data=payload)
c=response.text
b=(response.text).replace("true", '"true"').replace("null", '"null"').replace("-1",'"-1"')
print(c)






