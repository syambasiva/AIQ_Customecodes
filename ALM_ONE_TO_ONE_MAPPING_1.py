import argparse
import csv
import json
import os
import re
from datetime import date
from datetime import datetime
from pytz import timezone

import requests
import xmltodict

from ALM_ONE_TO_MANY_MAPPING import run


class UpdateStatusofjob:
    def __init__(self, kwargs):
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.environment = kwargs.get('environment')
        self.clientid = kwargs.get('clientid')
        self.secretid = kwargs.get('secretid')
        self.platformurl = kwargs.get('platformurl')
        self.AlmBaseUrl = kwargs.get('ALMURL')
        self.csvpath = kwargs.get('csvpath')
        self.domains = kwargs.get('domains')
        self.projects = kwargs.get('projects')

    def create_token(self, username, password, platformurl):
        url = '{}/v1/auth'.format(platformurl)

        response = requests.post(url, headers={'Content-Type': 'application/json'},
                                 json={'username': username, 'password': password, }, verify=False)

        if response.status_code != 200:
            print('Aiq token generation  API status code => {}, response =>{} '.format(response.status_code,
                                                                                       response.text))

        return json.loads(response.text)['token']

    def read_csv(self, csvpath):
        reader = csv.reader(open(csvpath))
        result = {}
        result1 = {}
        first_row = next(reader)
        for row in reader:
            key = row[0]
            val = row[5]
            if (val == 'Yes'):
                if key in result:
                    print(key)
                    pass
                result[key] = row[1:]

            if (val == 'No'):
                if key in result:
                    print(key)
                    pass
                result1[key] = row[1:]
        return result, result1

    def execution_status(self, gentoken, platform_url, value,key):
        print("value in API",value)
        url1 = '{}/v1/testexecutions/{}/getexecution'.format(platform_url, value)
        print("Reached Execution Status", url1)
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + gentoken
        }
        response = requests.request("GET", url1, headers=headers, data=payload, verify=False)
        if response.status_code != 200:
            print('Aiq Get Execution Status API status code => {}, response =>{} '.format(response.status_code,
                                                                                          response.text))
        res = json.loads(response.text)
        print(res)
        testcaseIds=key
        executionStatus=(res['statusMessage'])
        reportUrl=(res['reportUrl'])
        executionId=value

        print(testcaseIds)
        print(executionStatus)
        print(reportUrl)
        print(executionId)
        Testcase_Execution_status = dict(testcaseIds, executionStatus)
        test_Report = dict(testcaseIds, reportUrl)
        Testcase_Execution_id = dict(zip(testcaseIds, executionId))
        print(Testcase_Execution_id)
        print(Testcase_Execution_status)
        print(test_Report)
        return Testcase_Execution_status, test_Report, Testcase_Execution_id

    def ALM_cookie_generation(self, AlmBaseUrl, clientid, secretid):
        url = "{}/qcbin/rest/oauth2/login".format(AlmBaseUrl)
        print("ALM base url", url)
        payload = {'clientId': clientid, 'secret': secretid}
        print("payload ALM", payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, json=payload, verify=False)
        assert (
                response.status_code == 200), "error:Failed to Generate cookies please enter correct clientid={} && secreteid={} ".format(
            clientid, secretid)
        cookie_str = ''
        for i in response.cookies:
            cookie_str += "{}={};".format(i.name, i.value)
        return cookie_str

    def GetStatus(self, AlmBaseUrl, ALM_cookie, value, instanceurl):
        url = "{}/{}/test-sets/{}".format(AlmBaseUrl, instanceurl, value[0])
        print(url)
        payload = {}
        headers = {
            'Cookie': ALM_cookie,
        }
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        print(response)
        if response.status_code != 200:
            print('ALM Get TestSetStatus API Under TESTPLAN Status status code => {}, response =>{} '.format(
                response.status_code,
                response.text))
        url = "{}/{}/tests/{}".format(AlmBaseUrl, instanceurl, value[1])
        ##print(url)
        payload = {}
        headers = {
            'Cookie': ALM_cookie,
        }
        response1 = requests.request("GET", url, headers=headers, data=payload, verify=False)
        if response1.status_code != 200:
            print(
                'ALM Get TestidStatus TESTSET STATUS API status code => {}, response =>{} '.format(response.status_code,
                                                                                                   response.text))
        res1 = response1.content
        my_dict1 = xmltodict.parse(res1)
        json_data1 = my_dict1
        for i in json_data1['Entity']['Fields']['Field']:
            if i['@Name'] == 'status':
                TestidStatus_underTestPlan = i['Value']
            if i['@Name'] == 'user-template-06':
                Testcategory = i['Value']
        print("Testcategory value", Testcategory)
        res = response.content
        my_dict = xmltodict.parse(res)
        json_data = my_dict
        od1 = dict(json_data)
        for i in json_data['Entity']['Fields']['Field']:
            if i['@Name'] == 'status':
                TestSetStatus_UnderTestSeT = i['Value']
        Value = False
        if ((TestSetStatus_UnderTestSeT == "Draft" or TestSetStatus_UnderTestSeT == "Ready for Execution") and
                (TestidStatus_underTestPlan == "Draft" or TestidStatus_underTestPlan == "Approved")):
            Value = True
        return Value, Testcategory

    def Update_NotCompleTestinstance(self, AlmBaseUrl, ALM_cookie, value, instanceurl):

        url = "{}/{}/test-instances/{}".format(AlmBaseUrl, instanceurl, value[2])
        response = requests.request("PUT", url, headers={'Content-Type': 'application/json', 'Cookie': ALM_cookie, },
                                    json={"Fields": [{"Name": "status", "values": [{"value": "Not Completed"}]}]},
                                    verify=False)

    def Update_TestInstance(self, AlmBaseUrl, ALM_cookie, status, value, ExecutionId, instanceurl, environment):

        if status == "SUCCESS":
            status = "Passed"
        else:
            status = "Failed"

        url = "{}/{}/test-instances/{}".format(AlmBaseUrl, instanceurl, value[2])
        ExecutionID_updated = str(ExecutionId)

        ExecutionID_updated='4984'

        if (environment == "dev"):
            payload = {"Fields": [{"Name": "user-05", "values": [{"value": ExecutionID_updated}]},
                                  {"Name": "status", "values": [{"value": status}]}]}

        if (environment == "prod" or environment == "prod1"):
            payload = {"Fields": [{"Name": "user-11", "values": [{"value": ExecutionID_updated}]},
                                  {"Name": "status", "values": [{"value": status}]}]}

        headers = {
            'Content-Type': 'application/json',
            'Cookie': ALM_cookie,
        }
        response = requests.request("PUT", url, headers=headers, json=payload, verify=False)
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

    def Download_report(self, platformurl, gentoken, report):
        url = "{}/v1/downloadFile?fileURL={}".format(platformurl, report)

        payload = {}
        headers = {
            'Authorization': 'Bearer ' + gentoken
        }
        r = requests.get(url, headers=headers, data=payload, verify=False)
        assert (r.status_code == 200), "error:Message{} ".format(r.text)
        content = r.text
        with open('report.html', 'w') as f:
            f.write(content)

    def create_run(self, AlmBaseUrl, ALM_cookie, status, value, ExecutionIds, Testcategory, instanceurl, environment):

        today = date.today()

        now = datetime.now()
        fmt = "%H-%M-%S"
        now_time = datetime.now(timezone('US/Eastern'))

        if status == "SUCCESS":
            status = "Passed"
        else:
            status = "Failed"

        url = "{}/{}/runs".format(AlmBaseUrl, instanceurl)

        if (environment == "dev"):
            payload = "<Entity Type='run'>\r\n <Fields>\r\n  <Field Name='name'><Value>Fast_Run_{}_{}</Value></Field>\r\n " \
                      "<Field Name='test-instance'><Value>1</Value></Field>\r\n  <Field Name='cycle-id'><Value>{}</Value>" \
                      "</Field>\r\n <Field Name='test-id'><Value>{}</Value></Field>\r\n <Field Name='subtype-id'>" \
                      "<Value>hp.qc.run.MANUAL</Value></Field>\r\n <Field Name='status'><Value>{}</Value></Field>\r\n " \
                      "<Field Name=\"testcycl-id\"><Value>{}</Value></Field>\r\n " \
                      "<Field Name='owner'><Value>aiq_automation</Value></Field>\r\n " \
                      "<Field Name='user-template-07'><Value>Draft</Value></Field>" \
                      "<Field Name='user-template-10'><Value>Y</Value></Field>" \
                      "<Field Name='user-template-08'><Value>aiq_automation</Value></Field>" \
                      "<Field Name='user-template-09'><Value>{}</Value></Field>" \
                      "<Field Name='user-01'><Value>{}</Value></Field></Fields>\r\n</Entity>".format(
                now.strftime("%m-%d"),now_time.strftime(fmt), value[0], value[1], status, value[2], Testcategory,ExecutionIds)

        if (environment == "prod" or environment == "prod1"):
            payload = "<Entity Type='run'>\r\n <Fields>\r\n  <Field Name='name'><Value>Fast_Run_{}_{}</Value></Field>\r\n " \
                      "<Field Name='test-instance'><Value>1</Value></Field>\r\n  <Field Name='cycle-id'><Value>{}</Value>" \
                      "</Field>\r\n <Field Name='test-id'><Value>{}</Value></Field>\r\n <Field Name='subtype-id'>" \
                      "<Value>hp.qc.run.MANUAL</Value></Field>\r\n <Field Name='status'><Value>{}</Value></Field>\r\n " \
                      "<Field Name=\"testcycl-id\"><Value>{}</Value></Field>\r\n " \
                      "<Field Name='owner'><Value>aiq_automation</Value></Field>\r\n " \
                      "<Field Name='user-template-07'><Value>Draft</Value></Field>" \
                      "<Field Name='user-template-10'><Value>Y</Value></Field>" \
                      "<Field Name='user-template-08'><Value>aiq_automation</Value></Field>" \
                      "<Field Name='user-template-09'><Value>{}</Value></Field>" \
                      "<Field Name='user-02'><Value>{}</Value></Field></Fields>\r\n</Entity>".format(
                now.strftime("%m-%d"),now_time.strftime(fmt), value[0], value[1], status, value[2], Testcategory,4984)

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

    def get_header(self, token):
        return {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Authorization': "Bearer {}".format(token),
            'cache-control': "no-cache",
        }

    def get_request(self, url, params=None, headers=None):
        rsp = requests.get(url, json=params, headers=headers, verify=False)
        assert rsp.status_code == 200, 'API => {}, Response => {}'.format(url, rsp.text)
        return rsp

    def get_test_case_info(self, gentoken, platformurl, test_case_id):
        url = "{}/v1/testexecutions/{}/getexecution".format(platformurl,4984)
        ##print("url of aiq steps",url)

        response = self.get_request(url, headers=self.get_header(gentoken))
        ##print("get testcase info",response)

        if response.status_code != 200:
            print('Get testcase info API status code => {}, response =>{} '.format(response.status_code,
                                                                                   response.text))
        return json.loads(response.text)

    def final_result(self, gentoken, platformurl, test_case_id):

        final_list = []
        try:
            a = self.get_test_case_info(gentoken, platformurl, test_case_id)
            b = json.loads(a['Steps'])
            start, end, status, count = (0, 0, 5, 0)
            first_message, second_message, block_name = ('Not processed', 'Not processed', '')
            skip = False
            # [{},{},{},{},{}]
            final_list = []
            var_msg = ''
            for i in b:
                if re.findall(r"run\s+\${(.*)}", i['instr'], re.IGNORECASE) and i['isBlockStep'] == True:
                    for k in i.get('subInstructions'):
                        if k['instr'].lower().startswith('print'):
                            ##print(k['data'])
                            split_data = k['data'].split('|')
                            first_message = split_data[0]
                            second_message = split_data[1]
                            if k['status'] == '0':
                                var_msg = first_message
                            elif k['status'] == '5':
                                var_msg = second_message
                            else:
                                var_msg = "Not processed"
                            ss = dict(status=k['status'], message=var_msg)
                            final_list.append(ss)
                            if k['message'] == 'Not processed':
                                return

                if i['instr'].lower().startswith('print'):
                    split_data = i['data'].split('|')
                    first_message = split_data[0]
                    second_message = split_data[1]
                    if i['status'] == '0':
                        var_msg = first_message
                    elif i['status'] == '5':
                        var_msg = second_message
                    else:
                        var_msg = "Not processed"
                    ss = dict(status=i['status'], message=var_msg)
                    final_list.append(ss)
                    if i['message'] == 'Not processed':
                        return

        except Exception as e:
            print("Error {} ".format(e))
        finally:
            return final_list

    def Attach_Report(self, AlmBaseUrl, ALM_cookie, creationid, instanceurl):
        url = "{}/{}/runs/{}/attachments".format(AlmBaseUrl, instanceurl, creationid)
        filepath = os.path.abspath("report.html")
        files = open(filepath, "rb")
        headers = {
            'Content-Type': 'application/octet-stream',
            'Slug': 'report.html',
            'Cookie': ALM_cookie
        }
        response = requests.request("POST", url, headers=headers, data=files, verify=False)
        assert (response.status_code == 201), "error:Message{} ".format(response.text)

    def get_teststeps(self, AlmBaseUrl, ALM_cookie, creationid, instanceurl):
        url = "{}/{}/runs/{}/run-steps".format(AlmBaseUrl, instanceurl, creationid)
        payload = {}
        headers = {
            'Cookie': ALM_cookie,
        }
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        assert (response.status_code == 200), "error:Message{} ".format(response.text)
        res = (response.content)
        runstepid = []
        my_dict = xmltodict.parse(res)
        json_data = my_dict
        for i in json_data['Entities']['Entity']:
            for j in i['Fields']['Field']:
                if j['@Name'] == 'id':
                    runstepid.append(j['Value'])
        return runstepid

    def Updating_step_Result(self, AlmBaseUrl, ALM_cookie, i, j, creationid, instanceurl):

        url = "{}/{}/runs/{}/run-steps/{}".format(AlmBaseUrl, instanceurl, creationid, i)

        if j.get('status') == '0':
            val = 'Passed'
        else:
            val = 'Failed'
        payload = {"Fields": [{"Name": "status", "values": [{"value": val}]}]}

        headers = {
            'Content-Type': 'application/json',
            'Cookie': ALM_cookie
        }
        response = requests.request("PUT", url, headers=headers, json=payload, verify=False)
        assert (response.status_code == 200), "error:Message{} ".format(response.text)

    def Updating_ActualResuult(self, AlmBaseUrl, ALM_cookie, i, creationid, j, instanceurl):
        url = "{}/{}/runs/{}/run-steps/{}".format(AlmBaseUrl, instanceurl, creationid, i)
        payload = {"Fields": [{"Name": "actual", "values": [{"value": j.get('message')}]}]}

        headers = {
            'Content-Type': 'application/json',
            'Cookie': ALM_cookie
        }
        response = requests.request("PUT", url, headers=headers, json=payload, verify=False)
        assert (response.status_code == 200), "error:Message{} ".format(response.text)

    def run(self):
        try:

            if (self.environment == "dev"):
                instanceurl = "qcbin/rest/domains/{}/projects/{}".format(self.domains,self.projects)

            if (self.environment == "prod"):
                instanceurl = "qcbin/rest/domains/{}/projects/{}".format(self.domains,self.projects)

            if (self.environment == "prod1"):
                instanceurl = "qcbin/rest/domains/{}/projects/{}".format(self.domains,self.projects)


            ##AiQ Token generation
            gentoken = self.create_token(self.username, self.password, self.platformurl)

            csvIteration, csv = self.read_csv(self.csvpath)
            print("iteration value", csvIteration)
            print("value", csv)


            run(csvIteration, self.platformurl, self.AlmBaseUrl, self.clientid, self.secretid,self.environment,self.username,self.password,self.domains,self.projects)
            variable_1 = []
            for key, value in csv.items():
                print(value[3])
                print("value of testcaseid",key)
                status, report, ExecutionIds = self.execution_status(gentoken, self.platformurl, value[3],key)
                print(status,"\n",report,"\n",ExecutionIds)

                if int(key) in status:

                    ALM_cookie = self.ALM_cookie_generation(self.AlmBaseUrl, self.secretid, self.clientid)


                    TestInstanceStatus, Testcategory = self.GetStatus(self.AlmBaseUrl, ALM_cookie, value, instanceurl)

                    if TestInstanceStatus == True:

                        self.Update_NotCompleTestinstance(self.AlmBaseUrl, ALM_cookie, value, instanceurl)

                        TestInstance_update = self.Update_TestInstance(self.AlmBaseUrl, ALM_cookie, status[int(key)],
                                                                       value, ExecutionIds[int(key)], instanceurl,
                                                                       self.environment)

                        self.Download_report(self.platformurl, gentoken, report[int(key)])

                        creationid, creationstatus = self.create_run(self.AlmBaseUrl, ALM_cookie, status[int(key)],
                                                                     value, ExecutionIds[int(key)], Testcategory,
                                                                     instanceurl, self.environment)

                        variable_1.append(
                            {"TestInstanceID": value[2], "RunId": creationid, "Status": TestInstance_update})

                        if int(key) in ExecutionIds:
                            aiq_steps_list = self.final_result(gentoken, self.platformurl, ExecutionIds[int(key)])

                        self.Attach_Report(self.AlmBaseUrl, ALM_cookie, creationid, instanceurl)
                        if os.path.exists("report.html"):
                            os.remove("report.html")

                        getrunids = self.get_teststeps(self.AlmBaseUrl, ALM_cookie, creationid, instanceurl)

                        for i, j in zip(getrunids, aiq_steps_list):
                            self.Updating_step_Result(self.AlmBaseUrl, ALM_cookie, i, j, creationid, instanceurl)

                            self.Updating_ActualResuult(self.AlmBaseUrl, ALM_cookie, i, creationid, j, instanceurl)
                    else:
                        print(TestInstanceStatus, "Execution and instance Status is Not As expected")
                else:
                    print("Testcase Id in CSV and AIQ is Not Matching.Please check TestcaseID in CSV file")
                print(variable_1)

        except Exception as error:
            print(error)


def argument_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-AIQ_url", "--platformurl", type=str,
                        help="Please provide autonomiq server url")

    parser.add_argument("-HPQC_ENV", "--environment", type=str,
                        help="Please provide HPQC environment")

    parser.add_argument("-AIQ_user", "--username", type=str,
                        help="Please provide Autonomiq username", default='appuser')

    parser.add_argument("-AIQ_pass", "--password", type=str,
                        help="Please provide Autonomiq password", default='app123')

    parser.add_argument("-ALM_secretekey", "--secretid", type=str,
                        help="Please provide ALM secretid")

    parser.add_argument("-ALM_Clientid", "--clientid", type=str,
                        help="Please provide ALM clientid")

    parser.add_argument("-ALM_url", "--ALMURL", type=str,
                        help="Please provide ALM url")

    parser.add_argument("-csvfilePath", "--csvpath", type=str,
                        help="Please provide correct csv path")

    parser.add_argument("-domains", "--domains", type=str,
                        help="Please provide correct domain name")

    parser.add_argument("-projects", "--projects", type=str,
                        help="Please provide correct project name")

    args = parser.parse_args()
    return args.__dict__


if __name__ == '__main__':
    UpdateStatusofjob(argument_parser()).run()
