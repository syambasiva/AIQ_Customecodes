import json

import requests

url = "https://test.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9MwiKwcReohzlfKsMS0PHdD55qo.S6jwJprsvpWInZukuFjwe38MZCXLe3AJvz81rjfjo.0o5Rw3okL8t&client_secret=E6ABF6D240EAFBA8326EB40AD11032274EF5E87D2A0F8541908FA498601FCDAF&username=vinothini.varadaraj@canclsuat.testinator.com.sit&password=test@123"

payload={}
files={}
headers = {
  'Cookie': 'BrowserId=rtNTUCRNEe2j7oVltHyUEQ; CookieConsentPolicy=0:0; LSKey-c$CookieConsentPolicy=0:0'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
j = json.loads(response.text)
token = j['access_token']
print("FirstAPI",token)

##

import requests
import json

url = "https://cancapital--sit.sandbox.my.salesforce.com/services/apexrest/v1/partner/createapplication?="

payload = json.dumps({
  "loanDetails": {
    "loanPurpose": "Working Capital",
    "loanAmount": "20000.00"
  },
  "partnerDetails": {
    "partnerAPIKey": "67e319a32fc5a4a0e39ebeee43b4ccf0",
    "partnerEmail": "varadaraj@canclsuat.testinator.com"
  },
  "accountDetails": {
    "name": "SONIX  INC",
    "phone": "473-221-2124",
    "industry": "Business Services",
    "taxId": "714073107",
    "dba": "SONIX  INC",
    "businessStructureName": "Corporation",
    "stateOfFormation": "AZ",
    "bizStartDate": "1990-06-07",
    "billingStreet": "8700 MORRISSETTE DR",
    "billingBuildingNumber": "",
    "billingCity": "SPRINGFIELD",
    "billingState": "VA",
    "billingPostalCode": "30096",
    "billingCountry": "US"
  },
  "contactDetails": {
    "title": "CEO",
    "firstName": "DANIEL",
    "lastName": "CUPP",
    "email": "CUPP@canclsuat.testinator.com",
    "phone": "5732212122",
    "birthDate": "1969-11-01",
    "socialSecurityNumber": "666660163",
    "mailingStreet": "90 MCCHORD ST UNIT 50",
    "mailingBuildingNumber": "",
    "mailingCity": "HICKAM AFB",
    "mailingState": "HI",
    "mailingCountry": "US",
    "mailingPostalCode": "33140"
  }
})
headers = {
  'Authorization': 'OAuth {}'.format(token),
  'Content-Type': 'application/json',
  'Cookie': 'BrowserId=rtNTUCRNEe2j7oVltHyUEQ; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

response = requests.request("POST", url, headers=headers, data=payload)
j = json.loads(response.text)
ApplicationNumber=j[0]['ApplicationDetails']['Name']
print("SecondAPI",ApplicationNumber)
##
import requests

url = "https://cancapital--sit.sandbox.my.salesforce.com/services/apexrest/v1/partner/uploaddocs/?application={}&partnerEmail=varadaraj@canclsuat.testinator.com&name=109467.pdf&documentType=Bank Statements&contentType=applications/pdf&partnerAPIKey=67e319a32fc5a4a0e39ebeee43b4ccf0".format(ApplicationNumber)

payload="<file contents here>"
headers = {
   'Authorization': 'OAuth {}'.format(token),
  'Content-Type': 'application/pdf',
  'Cookie': 'BrowserId=rtNTUCRNEe2j7oVltHyUEQ; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("ThirdAPI",response.text)

import requests

url = "https://cancapital--sit.sandbox.my.salesforce.com/services/apexrest/v1/partner/processapplication/"

payload = "{\r\n    \"application\": \"APP-0000030254\",\r\n    \"consentAccepted\" : true,\r\n    \"partnerDetails\": {\r\n        \"partnerEmail\": \"varadaraj@canclsuat.testinator.com\",\r\n        \"partnerAPIKey\":\"67e319a32fc5a4a0e39ebeee43b4ccf0\"\r\n    }\r\n}"
headers = {
   'Authorization': 'OAuth {}'.format(token),
  'Content-Type': 'text/plain',
  'Cookie': 'BrowserId=rtNTUCRNEe2j7oVltHyUEQ; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
