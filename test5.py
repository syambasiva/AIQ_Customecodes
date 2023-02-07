import requests
import json

url1='https://thejoint.autonomiq.ai'
usn='thejointadmin'
pwd='Thejointadmin@123'
accountNumber=2
id=13


url = "{}/platform/v1/auth".format(url1)

payload = json.dumps({
  "username":usn ,
  "password": pwd
})
headers = {
  'Authorization': 'Basic YWRvYmVhZG1pbjpBZG9iZWFkbWluQDEyMw==',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

j = json.loads(response.text)
token = j['token']
print(token)

import requests

url = "{}/platform/discovery/{}/{}/testcases".format(url1,id,accountNumber)

payload={}
headers = {
  'Authorization': 'Bearer {}'.format(token)
}

response = requests.request("GET", url, headers=headers, data=payload)
res = json.loads(response.text)
TestcaseIds=[]
projectId=[]
browser = []
platform = []
Linux_And_Chrome=[]
Linux_And_firefox=[]
Windows_And_Chrome=[]
Windows_And_firefox=[]
Windows_And_edge=[]
Dummy=[]
for i in res:
    TestcaseIds.append(i['testCaseId'])
    projectId.append(i['discoveryId'])

print(TestcaseIds)
print(projectId)

Testcase_Execution_id = dict(zip(TestcaseIds,projectId))

print(type(Testcase_Execution_id))
print(Testcase_Execution_id)

for exe_id, Proj_id in Testcase_Execution_id.items():
    print(exe_id, ":", Proj_id)
    url = "{}/platform/testScriptExecutions/{}/{}/{}/-1/0/executions".format(url1,accountNumber,Proj_id,exe_id)

    payload = {}
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }

    response = requests.request("GET", url, headers=headers, data=payload,verify=False)
    status = json.loads(response.text)
    print(status)
    Platform=status['tasks']


    TaskLen=len(Platform)
    if(TaskLen !=0):
        if(Platform[0]['browser']=="chrome" and Platform[0]['platform']=="linux"):
            Linux_And_Chrome.append(Platform[0]['platform'])

        elif(Platform[0]['browser']=="firefox" and Platform[0]['platform']=="linux"):
            Linux_And_firefox.append(Platform[0]['platform'])

        elif (Platform[0]['browser'] == "chrome" and Platform[0]['platform'] == "windows 10"):
            Windows_And_Chrome.append(Platform[0]['platform'])

        elif (Platform[0]['browser'] == "firefox" and Platform[0]['platform'] == "windows 10"):
            Windows_And_firefox.append(Platform[0]['platform'])

        elif (Platform[0]['browser'] == "microsoftedge" and Platform[0]['platform'] == "windows 10"):
            Windows_And_edge.append(Platform[0]['platform'])
        else:
            print(Platform[0]['browser'])
            print(Platform[0]['platform'])


print(Linux_And_Chrome)
print(len(Linux_And_Chrome))
print(Linux_And_firefox)
print(len(Linux_And_firefox))
print(Windows_And_Chrome)
print(len(Windows_And_Chrome))
print(Windows_And_firefox)
print(len(Windows_And_firefox))
print(Windows_And_edge)
print(len(Windows_And_edge))
print("sonato")

    ##{'executionId': 468, 'executionName': 'First_scenario_suite1', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-08-29T17:30:02Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'jiPsdqlPsFmnXsaxV33MNCdqtQIFL7uwESlvWgGob7aOA4RgJRjONk3-IMkegdqK3GjiKoptWb8bOQyq1ylAj-U79XXO_HKhwwRakwzX-oPILLA4alYNa6ZUew9fhVfaS8mh9ntUtHXqUum230o=', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}
    ##[{'executionId': 468, 'executionName': 'First_scenario_suite1', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-08-29T17:30:02Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'jiPsdqlPsFmnXsaxV33MNCdqtQIFL7uwESlvWgGob7aOA4RgJRjONk3-IMkegdqK3GjiKoptWb8bOQyq1ylAj-U79XXO_HKhwwRakwzX-oPILLA4alYNa6ZUew9fhVfaS8mh9ntUtHXqUum230o=', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 23, 'executionName': 'First_scenario', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-08-09T15:07:31Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '../videos/23/zalenium_3c9ef98b_8a8c_4b68_b84d_566acf316db9_chrome_LINUX_20220809170729662_COMPLETED.mp4', 'reportUrl': '90OXVyOgkjkkzZktCRMKeVS-8_vkwhDWEpzlniidQGsyd2If1x9GcYZD7NS1H1SmerhfTSyhT-IG7YtlfTH37C6WWxI71QPMGFWz_wYekGR-lFDZaS6K8cZa6f81EuWaBDYvIS2-N0sWwtplvA==', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 10, 'executionName': 'First_scenario_suite2', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-07-30T05:23:27Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'BOscm0H4mSm55kef38_Ge2MepRiauDj4YPpLMOV7AbyXzju0e2FCLHxa7Q-RfBRiNjvhEuZwAm7qkig4b6Dc42ig_NWctQrCafVjwyDG7IxA2T6QuHfmAGmowWHb_4GYoxfQp5dxm1ANLAbQ', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 7, 'executionName': 'First_scenario', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-07-21T16:31:34Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'PeXb6_Lju9oXwxAwgRjh0nwIfk5P1AFsiakFPg-c2o-bsLEQq2rulNEFeaeGpzj6q1tbiLpousnnpqT8WilevPWpfeY8wwQGYoAir-cilf9rIOVApfHjD5ebr9NetBBn9QOf8A==', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 6, 'executionName': 'First_scenario', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-07-21T16:26:53Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'rE4GKf5sIA8UjUYjpEX3zloP_lmNhmaqC5QObwo_kPPgqqyu7aIfR5h-544QTccpbVeVJSFMgiq_prUYY3Aop-PGcoTvXoSBgz79zgkwDbf63Pl4v68rYLWOXO36j8-D7sA44A==', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 2, 'executionName': 'First_scenario_suite1', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-07-19T16:34:39Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'ei2bOlBKcTN_2OK-yZxGE2qtHBeePGkieG7fBWXuGC1chh2pH8b3NdIJ-2emh6glP807yEmyNN1pk4frtnCzi30uTLBNlpviGn-kBFyWBVbhxS8ENMTzlTrujhuANxK5jbMqaw==', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}]
    ##{'tasks': [{'executionId': 468, 'executionName': 'First_scenario_suite1', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-08-29T17:30:02Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'jiPsdqlPsFmnXsaxV33MNCdqtQIFL7uwESlvWgGob7aOA4RgJRjONk3-IMkegdqK3GjiKoptWb8bOQyq1ylAj-U79XXO_HKhwwRakwzX-oPILLA4alYNa6ZUew9fhVfaS8mh9ntUtHXqUum230o=', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 23, 'executionName': 'First_scenario', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-08-09T15:07:31Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '../videos/23/zalenium_3c9ef98b_8a8c_4b68_b84d_566acf316db9_chrome_LINUX_20220809170729662_COMPLETED.mp4', 'reportUrl': '90OXVyOgkjkkzZktCRMKeVS-8_vkwhDWEpzlniidQGsyd2If1x9GcYZD7NS1H1SmerhfTSyhT-IG7YtlfTH37C6WWxI71QPMGFWz_wYekGR-lFDZaS6K8cZa6f81EuWaBDYvIS2-N0sWwtplvA==', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 10, 'executionName': 'First_scenario_suite2', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-07-30T05:23:27Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'BOscm0H4mSm55kef38_Ge2MepRiauDj4YPpLMOV7AbyXzju0e2FCLHxa7Q-RfBRiNjvhEuZwAm7qkig4b6Dc42ig_NWctQrCafVjwyDG7IxA2T6QuHfmAGmowWHb_4GYoxfQp5dxm1ANLAbQ', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 7, 'executionName': 'First_scenario', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-07-21T16:31:34Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'PeXb6_Lju9oXwxAwgRjh0nwIfk5P1AFsiakFPg-c2o-bsLEQq2rulNEFeaeGpzj6q1tbiLpousnnpqT8WilevPWpfeY8wwQGYoAir-cilf9rIOVApfHjD5ebr9NetBBn9QOf8A==', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 6, 'executionName': 'First_scenario', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-07-21T16:26:53Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'rE4GKf5sIA8UjUYjpEX3zloP_lmNhmaqC5QObwo_kPPgqqyu7aIfR5h-544QTccpbVeVJSFMgiq_prUYY3Aop-PGcoTvXoSBgz79zgkwDbf63Pl4v68rYLWOXO36j8-D7sA44A==', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}, {'executionId': 2, 'executionName': 'First_scenario_suite1', 'executionStatus': 'SUCCESS', 'initiatedOn': '2022-07-19T16:34:39Z', 'projectName': 'Training_reference', 'projectId': 2, 'executionVideoUrl': '', 'reportUrl': 'ei2bOlBKcTN_2OK-yZxGE2qtHBeePGkieG7fBWXuGC1chh2pH8b3NdIJ-2emh6glP807yEmyNN1pk4frtnCzi30uTLBNlpviGn-kBFyWBVbhxS8ENMTzlTrujhuANxK5jbMqaw==', 'testcaseId': 3, 'testCaseName': 'First_scenario', 'tcErrors': 0, 'tcWarnings': 0, 'classes': None, 'aiqExecution': True, 'aiqReportData': '', 'browser': 'chrome', 'browserVersion': '', 'platform': 'linux', 'platform_version': '', 'appiumVersion': '', 'deviceName': '<nil>', 'deviceType': '', 'deviceOrientation': '', 'errorsCount': 0, 'warningsCount': 0, 'statusMessage': 'Success'}], 'total_execs': 6}

