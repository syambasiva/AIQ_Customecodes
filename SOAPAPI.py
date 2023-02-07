import requests

url = "https://www.w3schools.com/xml/tempconvert.asmx"
aiq_1=26
payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<soap12:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap12=\"http://www.w3.org/2003/05/soap-envelope\">\r\n  <soap12:Body>\r\n    <CelsiusToFahrenheit xmlns=\"https://www.w3schools.com/xml/\">\r\n      <Celsius>{}</Celsius>\r\n    </CelsiusToFahrenheit>\r\n  </soap12:Body>\r\n</soap12:Envelope>".format(aiq_1)
print(payload)
headers = {
  'Content-Type': 'application/soap+xml'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)