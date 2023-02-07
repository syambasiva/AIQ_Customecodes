import json

import requests
import xmltodict


def GetStatus(AlmBaseUrl,ALM_cookie,value):
    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/test-sets/{}".format(AlmBaseUrl,value[0])
    print(url)
    payload = {}
    headers = {
        'Cookie': ALM_cookie,
    }
    response = requests.request("GET", url, headers=headers, data=payload,verify=False)
    print(response)
    if response.status_code != 200:
        print('ALM Get TestSetStatus API Under TESTPLAN Status status code => {}, response =>{} '.format(response.status_code,
                                                                                      response.text))
    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/tests/{}".format(AlmBaseUrl, value[1])
    ##print(url)
    payload = {}
    headers = {
        'Cookie': ALM_cookie,
    }
    response1 = requests.request("GET", url, headers=headers, data=payload, verify=False)
    if response1.status_code != 200:
        print('ALM Get TestidStatus TESTSET STATUS API status code => {}, response =>{} '.format(response.status_code,
                                                                                      response.text))
    res1= response1.content
    my_dict1 = xmltodict.parse(res1)
    json_data1 = my_dict1
    ##print(json_data1)
    for i in json_data1['Entity']['Fields']['Field']:
        if i['@Name'] == 'status':
            TestidStatus_underTestPlan = i['Value']
        if i['@Name'] == 'user-template-06':
            Testcategory = i['Value']
    print("Testcategory value",Testcategory)
    ##print("Testidstatus",TestidStatus_underTestPlan)
    res = response.content
    ##print(res)
    my_dict = xmltodict.parse(res)
    json_data = my_dict
    od1 = dict(json_data)
    ##print(od1)
    for i in json_data['Entity']['Fields']['Field']:
        if i['@Name'] == 'status':
            TestSetStatus_UnderTestSeT = i['Value']
    ##print("testsetStatus",TestSetStatus_UnderTestSeT)
    Value = False
    if ((TestSetStatus_UnderTestSeT =="Draft" or TestSetStatus_UnderTestSeT== "Ready for Execution" ) and (TestidStatus_underTestPlan == "Draft" or TestidStatus_underTestPlan=="Approved")):
        Value = True
    return Value,Testcategory






