import argparse

import jwt
import time
import hashlib
import json
import requests
import csv


from aiq_api_handler import ApiTestHandler


def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True

class JWTGenerator:
    def __init__(self, account_id, access_key, secret_key, canonical_path):
        self.account_id = account_id
        self.access_key = access_key
        self.secret_key = secret_key
        self.expire = 3600
        self.canonical_path = canonical_path


    def jwt(self):
        payload = {
            'sub': self.account_id,
            'qsh': hashlib.sha256(self.canonical_path.encode('utf-8')).hexdigest(),
            'iss': self.access_key,
            'exp': time.time()+self.expire,
            'iat': time.time()
        }
        #print("payload======", payload)
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        ##print("token-------", token)
        return token
    @property
    def headers(self):
        headers = {
            'Authorization': 'JWT '+self.jwt(),
            'Content-Type': 'application/json',
            'zapiAccessKey': self.access_key
        }
        return headers

class UpdateReports:
    def __init__(self,account_id,access_key,secret_key,project_id,version_id,csvpath):
        self.token= None
        self.account_id = account_id
        self.access_key = access_key
        self.secret_key = secret_key
        self.project_id = project_id
        self.version_id = version_id
        self.csvpath = csvpath

    def createtoken(self,canonical_path):

        return JWTGenerator(self.account_id, self.access_key, self.secret_key, canonical_path).jwt()



    def updatereports_canonicalpath(self, execution_id,Issueid):
        return 'PUT&/public/rest/api/1.0/execution/' + execution_id + '&' + 'issueId=' + str(Issueid) + '&projectId=' + str(self.project_id)


    def update_result(self, execution_id,Issueid,id):
        updatereports_canonicalpath = self.createtoken(self.updatereports_canonicalpath(execution_id,Issueid))
        UpdateReports_id = self.update_Results(updatereports_canonicalpath,self.access_key,self.project_id,self.version_id,execution_id,Issueid,id)
        return UpdateReports_id

    def update_Results(self, token, access_key, project_id, version_id, execution_id, Issueid,id):
        ##print(token)
        url = 'https://prod-api.zephyr4jiracloud.com/connect/public/rest/api/1.0/execution/{}?issueId={}&projectId=10006'.format(
            execution_id, Issueid);
        headers2 = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'application/json',
            'zapiAccessKey': access_key
        }
        payload = {
            "issueId": Issueid,
            "projectId": project_id,
            "status": {
                "id": id
            },
            "versionId": version_id
        }
        result2 = requests.put(url, headers=headers2, json=payload)
        print(result2.status_code)
        if result2.status_code != 200:
          print('Get ResultsUpdate info API status code => {}, response =>{} '.format(result2.status_code,
                                                                                result2.text))
        return result2.status_code

    def csv_file_read(self,iteration_no):
        read_data = self.read_csv(iteration_no)
        return read_data

    def read_csv(self,iteration_no):
        ##print("csvfilepath ==>",self.csvpath)
        reader = csv.reader(open(self.csvpath))
        result = {}
        execution_id = None
        issue_id = None
        next(reader)  # skip collumn
        for index, row in enumerate(reader):
            ##print("iteration number in block",iteration_no)
            ##print("Index => ", index)
            if index == iteration_no:
                execution_id = row[1]
                issue_id = row[0]
        return execution_id, issue_id




def main(kwarg):
    base_url = kwarg.get("platformurl")
    user = kwarg.get("username")
    password = kwarg.get("password")
    account_id = kwarg.get("account_id")
    access_key = kwarg.get("access_key")
    secret_key = kwarg.get("secret_key")
    project_id = kwarg.get("project_id")
    version_id = kwarg.get("version_id")
    csvpath    = kwarg.get("csvpath")
    suiteid   =  kwarg.get("suiteid")
    TestcaseId = kwarg.get("TestcaseID")

    helper = ApiTestHandler(base_url, user, password, suiteid, TestcaseId)
    helper.set_token()

    helper.execution_ID()
    res = helper.get_test_case_info()
    resultData = res['resultData']
    IterationStatus = []
    for i in resultData:
        resultData1 = (i['resultData'])
        ##print("Result of Iteration",resultData1)
        if resultData1:
            for j in resultData1["iterationResult"]:
                print("value of j",j)
                iterationResult = (resultData1["iterationResult"])
                ##print("Iteration result data",iterationResult)
                for iteration_no, k in enumerate(iterationResult):
                    print(iteration_no)
                    print(k["is_success"])
                    if (k["is_success"]) == True:
                        id = 1
                        ##print(id)
                    else:
                        id = 2






def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-AIQ_url", "--platformurl", type=str,
                        help="Please provide autonomiq server url")

    parser.add_argument("-AIQ_user", "--username", type=str,
                        help="Please provide Autonomiq username", default='appuser')

    parser.add_argument("-AIQ_pass", "--password", type=str,
                        help="Please provide Autonomiq password", default='app123')

    parser.add_argument("-AIQ_suite_id", "--suiteid", type=int,
                        help="Please provide account suiteId")

    parser.add_argument("-AIQ_TC_id", "--TestcaseID", type=int,
                        help="Please provide account Testcaseid")

    parser.add_argument("-Zephyre_Accountid", "--account_id", type=str,
                        help="Please provide Zephyre AccountId")

    parser.add_argument("-Zephyre_accesskey", "--access_key", type=str,
                        help="Please provide Zephyre accessKey")

    parser.add_argument("-Zephyre_secretkey", "--secret_key", type=str,
                        help="Please provide Zephyre secretkey")

    parser.add_argument("-Zephyre_project_id", "--project_id", type=int,
                        help="Please provide Zephyre Projectid")

    parser.add_argument("-Zephyre_version_id", "--version_id", type=int,
                        help="Please provide Zephyre versionid")

    parser.add_argument("-csvpath", "--csvpath", type=str,
                        help="Please provide Zephyre csvpath")


    args = parser.parse_args()
    return args.__dict__


if __name__ == '__main__':

   main(argument_parser())







