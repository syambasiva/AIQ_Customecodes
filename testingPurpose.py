import csv
import os
import re

import requests
import json

import xmltodict
from datetime import date
from datetime import datetime
from pytz import timezone

from AttachReportsToRun import Attach_Report
from GetTeststepsofRun import get_teststeps
from UpdateActualResults import Updating_ActualResuult



def final_result(b):
  final_list = []
  try:
    final_list = []
    var_msg = ''
    for i in b:
        if i['instrType'] == "SimpleForLoopInstructionGroup":
            stepResultdata = (i['resultData'])
            print("final print",stepResultdata)
            res1 = (stepResultdata["iterationResult"][0])
            print("After final print",res1)
            b1 = res1['steps']
            print("value final",b1)
            for i in b1:
                a=i['instr']
                if i['instr'].lower().startswith('print'):
                    split_data = i['data'].split('|')
                    first_message = split_data[0]
                    second_message = split_data[1]
                    if i['status'] == 0:
                        var_msg = first_message
                    elif i['status'] == 5:
                        var_msg = second_message
                    else:
                        var_msg = "Not processed"
                    ss = dict(status=i['status'], message=var_msg)
                    final_list.append(ss)
                    if i['message'] == 'Not processed':
                        return

        if i['instrType'] == "SingleInstructionGroup":
                if i['instr'].lower().startswith('print'):
                    split_data = i['data'].split('|')
                    first_message = split_data[0]
                    second_message = split_data[1]
                    if i['status'] == 0:
                        var_msg = first_message
                    elif i['status'] == 5:
                        var_msg = second_message
                    else:
                        var_msg = "Not processed"
                    ss = dict(status=i['status'], message=var_msg)
                    final_list.append(ss)
                    if i['message'] == 'Not processed':
                        return


    print(final_list)

  except Exception as e:
    print("Error {} ".format(e))
  finally:
    return final_list

def Download_report(platformurl,tokenres,TestcaseId,ExecutionId_value,instrNumber,itrnum):
    url = "{}/v1/testacases/{}/testexecutions/{}/instructions/{}/iterations/{}/getdatadrivenreport".format(platformurl,TestcaseId,ExecutionId_value,instrNumber,itrnum)
    print("report Url",url)
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + tokenres
    }
    print("before download report")
    r = requests.get(url,headers=headers, data=payload,verify=False)
    assert (r.status_code == 200), "error:Message{} ".format(r.text)
    print("after download report")
    content = r.text
    with open('report12.html', 'w') as f:
        f.write(content)

def read_csv():
    reader = csv.reader(open("C:\\Users\\samba\\Downloads\\New folder\\SampledataforIteration.csv"))
    result = {}
    first_row = next(reader)
    for row in reader:
            key = row[0]
            if key in result:
                pass
            result[key] = row[1:]
    return result

def fetchfailedstep(tokenres,stepslen):
    url = "https://customersuccess.autonomiq.ai/platform/testCases/getTestCaseInfo/877/-1"

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + tokenres
    }

    response1 = requests.request("GET", url, headers=headers, data=payload)

    resGetTest = json.loads(response1.text)
    print(resGetTest)
    val1 = resGetTest['test_steps']
    val2 = json.loads(val1)
    print("steps of normal",val2)

    successmessage = []
    failedmessage = []
    for i in val2:
        if i['instr'].lower().startswith('print'):
            split_data = i['data'].split('|')
            first_message = split_data[0]
            second_message = split_data[1]
            successmessage.append(first_message)
            failedmessage.append(second_message)
        if re.findall(r"run\s+\${(.*)}", i['instr'], re.IGNORECASE) and i['isBlockStep'] == True:
            for k in i.get('subInstructions'):
                if k['instr'].lower().startswith('print'):
                    ##print(k['data'])
                    split_data = k['data'].split('|')
                    first_message = split_data[0]
                    second_message = split_data[1]
                    successmessage.append(first_message)
                    failedmessage.append(second_message)

    print(successmessage)
    failedvalue = dict(status=5, message=failedmessage[stepslen])
    return failedvalue


def execution_status(tokenres,platformurl,AIQsuiteId):
    ##url = '{}/v1/jobs/{}/2/get_executions'.format(platform_url, suiteid)
    url1 = '{}/v1/jobs/{}/2/get_executions'.format(platformurl,AIQsuiteId[0])
    print(url1)
    ##print("url for suite id",url1)
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + tokenres
    }
    response = requests.request("GET", url1, headers=headers, data=payload,verify=False)
    if response.status_code != 200:
        print('Aiq Get Execution Status API status code => {}, response =>{} '.format(response.status_code,response.text))
    res = json.loads(response.text)

    #print("response of Execution",res)
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
    return Testcase_Execution_id

def ALM_cookie_generation(AlmBaseUrl,clientid,secretid):
    url = "{}/qcbin/rest/oauth2/login".format(AlmBaseUrl)
    payload = {'clientId':clientid , 'secret':secretid}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, json=payload,verify=False)
    assert (response.status_code == 200), "error:Failed to Generate cookies please enter correct clientid={} && secreteid={} ".format(clientid,secretid)
    cookie_str = ''
    for i in response.cookies:
        cookie_str += "{}={};".format(i.name, i.value)
    return cookie_str

def Update_TestInstance(AlmBaseUrl, ALM_cookie,IterationStatus,TestInstanceIds1,ExecutionId_value):

    if IterationStatus == True:
        status = "Passed"
    else:
        status = "Failed"
    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/test-instances/{}".format(AlmBaseUrl,TestInstanceIds1)
    ExecutionID_updated = str(ExecutionId_value)
    #print(ExecutionID_updated)
    payload = {"Fields": [{"Name": "user-05", "values": [{"value":ExecutionID_updated}]},{"Name": "status", "values": [{"value":status }]}]}
    #print(payload)
    headers = {
          'Content-Type': 'application/json',
          'Cookie':ALM_cookie,
    }
    response = requests.request("PUT", url, headers=headers, json=payload,verify=False)
    print(response.status_code)
    if response.status_code != 200:
        print('Test Instance Status Update => {}, response =>{} '.format(response.status_code,
                                                                                      response.text))

    res = (response.content)
    print(response)
    my_dict = xmltodict.parse(res)
    runid = None
    runstatus = None
    json_data = my_dict
    for run in json_data['Entity']['Fields']['Field']:
        if run['@Name'] == 'status':
            runstatus = run['Value']
    return runstatus


def create_run(AlmBaseUrl, ALM_cookie, IterationStatus,TestSetIds1,TestIds1,TestInstanceIds1,ExecutionId_value):

    today = date.today()

    now = datetime.now()
    fmt = "%H-%M-%S"
    now_time = datetime.now(timezone('US/Eastern'))

    if IterationStatus == True:
        status = "Passed"
    else:
        status = "Failed"

    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/runs".format(AlmBaseUrl)

    payload = "<Entity Type='run'>\r\n <Fields>\r\n  <Field Name='name'><Value>Fast_Run_{}_{}</Value></Field>\r\n " \
              "<Field Name='test-instance'><Value>1</Value></Field>\r\n  <Field Name='cycle-id'><Value>{}</Value>" \
              "</Field>\r\n <Field Name='test-id'><Value>{}</Value></Field>\r\n <Field Name='subtype-id'>" \
              "<Value>hp.qc.run.MANUAL</Value></Field>\r\n <Field Name='status'><Value>{}</Value></Field>\r\n " \
              "<Field Name=\"testcycl-id\"><Value>{}</Value></Field>\r\n " \
              "<Field Name='owner'><Value>aiq_automation</Value></Field>\r\n " \
              "<Field Name='user-template-07'><Value>Draft</Value></Field>"\
              "<Field Name='user-template-10'><Value>Y</Value></Field>"\
              "<Field Name='user-template-08'><Value>aiq_automation</Value></Field>" \
              "<Field Name='user-01'><Value>{}</Value></Field></Fields>\r\n</Entity>".format(now.strftime("%m-%d"),now_time.strftime(fmt),
                                                                                                       TestSetIds1,
                                                                                                       TestIds1, status,
                                                                                                       TestInstanceIds1,ExecutionId_value)

    print(payload)
    headers = {
        'Content-Type': 'application/xml',
        'Accept': 'application/xml',
        'Cookie': ALM_cookie
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    assert (
            response.status_code == 201), "error: Failed to create Run. field is missing find in Error message \n ERRORMESSAGE:{}".format(
        response.text)
    res = (response.content)
    my_dict = xmltodict.parse(res)
    runid = None
    runstatus = None
    json_data = my_dict
    for run in json_data['Entity']['Fields']['Field']:
        if run['@Name'] == 'id':
            runid = run['Value']
        if run['@Name'] == 'status':
            runstatus = run['Value']
    return runid, runstatus

def Attach_Report(AlmBaseUrl,ALM_cookie,creationid):
    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/runs/{}/attachments".format(AlmBaseUrl,creationid)
    filepath = os.path.abspath("report12.html")
    files = open(filepath, "rb")
    headers = {
      'Content-Type': 'application/octet-stream',
       'Slug': 'report.html',
        'Cookie': ALM_cookie
    }
    response = requests.request("POST", url, headers=headers, data=files,verify=False)
    assert (response.status_code == 201), "error:Message{} ".format(response.text)

def Updating_step_Resultalm(AlmBaseUrl,ALM_cookie, i,j,creationid):

    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/runs/{}/run-steps/{}".format(AlmBaseUrl,creationid,i)

    if j.get('status') == 0:
        val = 'Passed'
    else:
        val = 'Failed'
    payload = {"Fields": [{"Name": "status", "values": [{"value": val}]}]}


    headers = {
        'Content-Type': 'application/json',
        'Cookie': ALM_cookie
    }
    response = requests.request("PUT", url, headers=headers, json=payload,verify=False)
    assert (response.status_code == 200), "error:Message{} ".format(response.text)

def run():

    csviteration = read_csv()
    #print(csviteration)
    #csviteration = {'983': ['2837,2837,2387,2387,2387', '2659,2659,2659,2659', '20432,20432,20433,20434', '94', 'Yes'], '9831': ['2837,2837,2387,2387,2387', '2659,2659,2659,2659', '20432,20432,20433,20434', '94', 'Yes']}
    for key, value in csviteration.items():
        val = csviteration[key]
        TestcaseId=key
        #print("testcaseId",TestcaseId)
        list = []
        for i in val:
            list.append(i.split(','))
        TestSetIds=(list[0])
        TestIds=(list[1])
        TestInstanceIds=(list[2])
        AIQsuiteId=(list[3])
        #print("setid",TestSetIds)
        #print("testid",TestIds)
        #print("instid",TestInstanceIds)
        #print(AIQsuiteId[0])
        #print("reached step1",TestIds)

        platformurl="https://customersuccess.autonomiq.ai/platform"
        AlmBaseUrl ="http://useqawapqc01.na.ivc:8080"
        clientid= "apikey-keeghmctolkfodhgpqpf"
        secretid= "fbbhkcmcndbmlfii"

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
        tokenres=json.loads(response.text)['token']
        #print(tokenres)

        ExecutionId=execution_status(tokenres,platformurl,AIQsuiteId)
        #print(ExecutionId)
        #ExecutionId_value=(ExecutionId[int(key)])
        #print(ExecutionId_value)
        ExecutionId_value=91
        #https://qa1.autonomiq.ai/platform/v1/testexecutions/218525/getexecution
        url = "{}/v1/testexecutions/{}/getexecution".format(platformurl,ExecutionId_value)
        #print(url)

        payload={}
        headers = {
        'Authorization': 'Bearer ' + tokenres
            }

        response = requests.request("GET", url, headers=headers, data=payload)
        #print("response execution")
        resGetTest = json.loads(response.text)

        resultData = resGetTest['resultData']
        #print("result data",resultData)
        for i in resultData:
            resultData1 = (i['resultData'])
            print("result data1",resultData1)
            if resultData1:
                numberofIterations = len(resultData1["iterationResult"])
                instrNumber = i['instrNum']
                print(numberofIterations)
                variable_1 = []
                for i in range(numberofIterations):
                    itrnum = i +1
                    IterationStatus1 = (resultData1["iterationResult"][i])
                    IterationStatus=(IterationStatus1['is_success'])
                    print("iteration status",IterationStatus)
                    res = (resultData1["iterationResult"][i])
                    print("iteration steps",res)
                    b = res['steps']
                    print("values of aiq",b)
                    aiq_steps_list =final_result(b)
                    stepslen=(len(aiq_steps_list))
                    print("steps of AIQ",aiq_steps_list)
                    if IterationStatus == False:
                        Failstep = fetchfailedstep(tokenres,stepslen)
                        aiq_steps_list.append(Failstep)
                        print("print steps",aiq_steps_list)
                    report=Download_report(platformurl,tokenres,TestcaseId,ExecutionId_value,instrNumber,itrnum)
                    print("Iterations",i,TestSetIds[i])
                    print("Iterations",i,TestIds[i])
                    print("Iterations",i,TestInstanceIds[i])
                    ALM_cookie=ALM_cookie_generation(AlmBaseUrl,clientid,secretid)
                    instanceurl = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/test-instances/{}".format(AlmBaseUrl,TestInstanceIds[i])
                    print(instanceurl)
                    UpdateInstance_response = requests.request("PUT", instanceurl,headers={'Content-Type': 'application/json', 'Cookie': ALM_cookie,},
                    json={"Fields": [{"Name": "status", "values": [{"value": "Not Completed"}]}]},verify=False)
                    print(UpdateInstance_response)
                    TestSetIds1 = TestSetIds[i]
                    TestIds1 = TestIds[i]
                    TestInstanceIds1 = TestInstanceIds[i]
                    updatetestinstance = Update_TestInstance(AlmBaseUrl,ALM_cookie,IterationStatus,TestInstanceIds1,ExecutionId_value)
                    print("instance status",updatetestinstance)
                    creationid, creationstatus=create_run(AlmBaseUrl,ALM_cookie,IterationStatus,TestSetIds1,TestIds1,TestInstanceIds1,ExecutionId_value)
                    print("creation Id Run ID",creationid)
                    print("Run status",creationstatus)
                    print("TestInstanceID: " + TestInstanceIds1 + "   RunId: " + creationid + "   Status: " + updatetestinstance)
                    reportattachment=Attach_Report(AlmBaseUrl,ALM_cookie,creationid)
                    if os.path.exists("report12.html"):
                        os.remove("report12.html")
                    getrunids=get_teststeps(AlmBaseUrl, ALM_cookie, creationid)
                    variable_1.append({"TestInstanceID": TestInstanceIds1, "RunId": creationid, "Status": updatetestinstance})
                    print("get run ids for run",getrunids)
                    for i, j in zip(getrunids, aiq_steps_list):
                        updating_alm_steps=Updating_step_Resultalm(AlmBaseUrl,ALM_cookie, i,j,creationid)
                        updateActualResult = Updating_ActualResuult(AlmBaseUrl, ALM_cookie, i, creationid, j)
                print("End of iteration",i,variable_1)

if __name__ == '__main__':
  run()









