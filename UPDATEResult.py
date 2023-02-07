import argparse

import jwt
import time
import hashlib
import json
import requests
import csv


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

        print("accountid",self.account_id)
        print("access key",self.access_key)
        print("secrete key",self.secret_key)
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
        print("token-------", token)
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

    def update_result(self, execution_id,Issueid):
        print(execution_id)
        print(Issueid)
        updatereports_canonicalpath = self.createtoken(self.updatereports_canonicalpath(execution_id,Issueid))
        UpdateReports_id = self.update_Results(updatereports_canonicalpath,self.access_key,self.project_id,self.version_id,execution_id,Issueid)
        return UpdateReports_id

    def update_Results(self,token,access_key, project_id, version_id,execution_id,Issueid):
        url = 'https://prod-api.zephyr4jiracloud.com/connect/public/rest/api/1.0/execution/{}?issueId={}&projectId=10006'.format(execution_id,Issueid);
        headers2 = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'application/json',
            'zapiAccessKey': access_key
        }
        payload = {
            "issueId": Issueid,
            "projectId": project_id,
            "status": {
                "id": "3"
            },
            "versionId": version_id
        }
        result2 = requests.put(url, headers=headers2, json=payload)
        print(result2.status_code)
        return result2.status_code

    def csv_file_read(self):
        read_data = self.read_csv()
        print(read_data)
        return read_data

    def read_csv(self):
        print("csv file path", csvpath)
        reader = csv.reader(open(self.csvpath))
        result = {}
        first_row = next(reader)
        for row in reader:
            key = row[0]
            if key in result:
                pass
            result[key] = row[1:]
        return result

    def run(self):

        csv = self.csv_file_read()
        print(csv)
        for key,value in csv.items():
            self.update_result(value[0],key)

def main(kwarg):

    account_id = kwarg.get("account_id")
    access_key = kwarg.get("access_key")
    secret_key = kwarg.get("secret_key")
    project_id = kwarg.get("project_id")
    version_id = kwarg.get("version_id")
    csvpath    = kwarg.get("csvpath")

    helper_update_reports = UpdateReports(account_id, access_key, secret_key, project_id, version_id, csvpath)
    csvfile=helper_update_reports.csv_file_read()
    print(csvfile)
    for key, value in csvfile.items():
        helper_update_reports.update_result(value[0],key)




def argument_parser():
    parser = argparse.ArgumentParser()

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
    csvpath = "C:\\Users\\samba\\Downloads\\IntegrationFile\\ZephyreIntegration.csv"
    account_id = '5fbb6f2acbead5006917e2d8'
    access_key = 'YzRmMWRlM2ItY2M1ZS0zMjcwLTk5MmUtYjQ0MjVhZDZjNzFlIDVmYmI2ZjJhY2JlYWQ1MDA2OTE3ZTJkOCBVU0VSX0RFRkFVTFRfTkFNRQ'
    secret_key = 'm2143WjBOMJMOFqq1wLQvCExbU55vPBDLv5GozZPzVE'
    project_id= 10006
    version_id= -1
    UpdateReports(account_id,access_key,secret_key,project_id,version_id,csvpath).run()
    main(argument_parser())







