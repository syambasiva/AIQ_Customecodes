import argparse
import os

import requests

from AIQTokenGeneration import create_token
from ALMCookieGeneration import ALM_cookie_generation
from ALMCreaterun import create_run
from AttachReportsToRun import Attach_Report
from DownloadReport import Download_report
from GetExecutionStatus import execution_status
from GetStatus_TestsetAnd_instance import GetStatus
from GetTeststepsofRun import get_teststeps
from UpdateInstanceid import Update_TestInstance
from UpdatingTeststepRunStatus import Updating_step_Result
from csvfileupload import read_csv
from UpdateActualResults import Updating_ActualResuult
from get_AIQ_steps import final_result
from ALM_ONE_TO_MANY import run


class UpdateStatusofjob:
    def __init__(self, kwargs):
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        # self.suiteid = kwargs.get('suiteid')
        self.clientid = kwargs.get('clientid')
        self.secretid = kwargs.get('secretid')
        self.platformurl = kwargs.get('platformurl')
        self.AlmBaseUrl = kwargs.get('ALMURL')
        self.csvpath = kwargs.get('csvpath')

    def get_token(self):
        token = create_token(self.username, self.password, self.platformurl)
        return token

    def get_execution_status(self, gentoken, value):
        get_status, reporturl, ExecutionID = execution_status(gentoken, self.platformurl, value)
        return get_status, reporturl, ExecutionID

    def get_cookie(self):
        cookie = ALM_cookie_generation(self.AlmBaseUrl, self.secretid, self.clientid)
        return cookie

    def create_run(self, ALM_cookie, status, value, ExecutionIds,Testcategory):
        runid, runstatus = create_run(self.AlmBaseUrl, ALM_cookie, status, value,ExecutionIds,Testcategory)
        return runid, runstatus

    def Update_instance_status(self, ALM_cookie, status, value,ExecutionId):
        Instance_status = Update_TestInstance(self.AlmBaseUrl, ALM_cookie, status, value,ExecutionId)
        return Instance_status

    def Get_status(self, AlmBaseUrl, ALM_cookie, value):
        status,Testcategory = GetStatus(AlmBaseUrl, ALM_cookie, value)
        return status,Testcategory

    def csv_file_read(self):
        read_data = read_csv(self.csvpath)
        return read_data

    def getstStatus(self, ALM_cookie, creationid):
        runstepid = get_teststeps(self.AlmBaseUrl, ALM_cookie, creationid)
        return runstepid

    def download_report(self, gentoken, report):
        Download_report(self.platformurl, gentoken, report)

    def Attach_reports_toruns(self, ALM_cookie, creationid):
        Attachment = Attach_Report(self.AlmBaseUrl, ALM_cookie, creationid)

    def run(self):
        try:
            gentoken = self.get_token()
            print(gentoken)

            csvIteration,csv = self.csv_file_read()
            print("csv normal",csv)
            print("csv Iterations",csvIteration)

            run(csvIteration, self.platformurl, self.AlmBaseUrl, self.clientid, self.secretid)
            variable_1 = []
            for key, value in csv.items():

                if value[3] == '':
                    print("key for empty suite", key)
                else:
                    status, report, ExecutionIds = self.get_execution_status(gentoken, value)
                if int(key) in status:

                    ALM_cookie = self.get_cookie()
                    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/test-instances/{}".format(self.AlmBaseUrl,
                                                                                                     value[2])
                    response = requests.request("PUT", url,
                                                headers={'Content-Type': 'application/json', 'Cookie': ALM_cookie, },
                                                  json={
                                                    "Fields": [
                                                        {"Name": "status", "values": [{"value": "Not Completed"}]}]},
                                                verify=False)
                    TestInstanceStatus,Testcategory = self.Get_status(self.AlmBaseUrl, ALM_cookie, value)
                    if TestInstanceStatus == True:
                        TestInstance_update = self.Update_instance_status(ALM_cookie, status[int(key)], value,
                                                                          ExecutionIds[int(key)])
                        download_report = self.download_report(gentoken, report[int(key)])
                        creationid, creationstatus = self.create_run(ALM_cookie, status[int(key)], value,
                                                                     ExecutionIds[int(key)],Testcategory)
                        print("TestInstanceID: " + value[
                            2] + "   RunId: " + creationid + "   Status: " + TestInstance_update)

                        variable_1.append(
                            {"TestInstanceID": value[2], "RunId": creationid, "Status": TestInstance_update})

                        if int(key) in ExecutionIds:
                            aiq_steps_list = final_result(gentoken, self.platformurl, ExecutionIds[int(key)])

                        Reports_attachment = self.Attach_reports_toruns(ALM_cookie, creationid)
                        if os.path.exists("report.html"):
                            os.remove("report.html")
                        getrunids = self.getstStatus(ALM_cookie, creationid)

                        for i, j in zip(getrunids, aiq_steps_list):
                            update = Updating_step_Result(self.AlmBaseUrl, ALM_cookie, i, j, creationid)

                            updateActualResult = Updating_ActualResuult(self.AlmBaseUrl, ALM_cookie, i, creationid, j)
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

    # parser.add_argument("-AIQ_suite_id", "--suiteid", type=int,
    # help="Please provide account id")

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

    args = parser.parse_args()
    return args.__dict__


if __name__ == '__main__':
    UpdateStatusofjob(argument_parser()).run()
