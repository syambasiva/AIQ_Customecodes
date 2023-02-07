import requests
import json

url = "https://cancapital--qaautomat1.my.salesforce.com/services/apexrest/v1/partner/processapplication"

payload = {'application': 'APP-0000022405','consentAccepted' : True,'partnerDetails': {'partnerEmail': 'percentage.broker@canclsuat.testinator.com','partnerAPIKey':'56ac9d75a95aaaafe04e22b89dc118c9'}}


BearerToken="00D8G0000008hsB!ARYAQCLABEaDYXQCIjphB35kosyjgqRSehvZCZqUTm6rffp14bGFjlElBT7lpUTWjObGPcXWe2hFu3.RskRU1yv9PXP8kM.9"
headers = {
  'Authorization': 'OAuth '+BearerToken,
  'Content-Type': 'application/json',
  'Cookie': 'BrowserId=6mp6OpksEey-iXXIwzxhwQ; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


