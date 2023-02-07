import json

import requests


def execution_status(gentoken,platform_url,value):
    ##url = '{}/v1/jobs/{}/2/get_executions'.format(platform_url, suiteid)
    url1 = '{}/v1/jobs/{}/2/get_executions'.format(platform_url,value[3])
    print(url1)
    ##print("url for suite id",url1)
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + gentoken
    }
    response = requests.request("GET", url1, headers=headers, data=payload,verify=False)
    if response.status_code != 200:
        print('Aiq Get Execution Status API status code => {}, response =>{} '.format(response.status_code,response.text))
    res = json.loads(response.text)


    job = res['jobs'][0]
    testcaseIds = []
    executionStatus = []
    reportUrl = []
    executionId=[]
    for task in job['etrs']['tasks']:
        testcaseIds.append(task['testcaseId'])
        executionStatus.append(task['executionStatus'])
        reportUrl.append(task['reportUrl'])
        executionId.append(task['executionId'])


    Testcase_Execution_status = dict(zip(testcaseIds, executionStatus))
    test_Report = dict(zip(testcaseIds, reportUrl))
    Testcase_Execution_id = dict(zip(testcaseIds,executionId))
    return Testcase_Execution_status,test_Report,Testcase_Execution_id
