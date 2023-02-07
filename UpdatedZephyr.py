import argparse
import json
import jwt
import time
import hashlib
import requests
import csv



JWT_EXPIRE = 3600
USER = 'admin'


class main:
    def __init__(self, kwargs):
        self.platformurl=kwargs.get('platformurl')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.account_id = kwargs.get('account_id')
        self.access_key = kwargs.get('access_key')
        self.secret_key = kwargs.get('secret_key')
        self.csvpath = kwargs.get('csvpath')
        self.Zephyrurl = kwargs.get('Zephyrurl')

    def read_csv(self, csvpath):
        reader = csv.reader(open(csvpath))

        first_row = next(reader)
        for row in reader:
            print(row)
        return row

    def FetchReleaseAndProjectId(self,PROJECT_NAME,RELEASE_NAME):

        RELATIVE_PATH = '/public/rest/api/1.0/zql/fields/values'
        CANONICAL_PATH = 'GET&' + RELATIVE_PATH + '&'
        payload_token = {
            'sub': USER,
            'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
            'iss': self.access_key,
            'exp': int(time.time()) + JWT_EXPIRE,
            'iat': int(time.time())
        }
        token = jwt.encode(payload_token, self.secret_key, algorithm='HS256').strip().decode('utf-8')
        headers = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'text/plain',
            'zapiAccessKey': self.access_key
        }
        raw_result1 = requests.get(self.Zephyrurl + RELATIVE_PATH, headers=headers)
        json_result = json.loads(raw_result1.text)
        versionid = json_result['fields']['fixVersion']
        projectid = json_result['fields']['project']
        for i in projectid:
            if i['name'] == PROJECT_NAME:
                PROJECT_ID = (i['id'])
        for i in versionid:
            if i['name'] == RELEASE_NAME:
                VERSION_ID = (i['id'])
        return PROJECT_ID, VERSION_ID

    def fetchCycle_Id(self,PROJECT_ID,VERSION_ID,CYCLE_NAME):

        RELATIVE_PATH = '/public/rest/api/1.0/cycles/search?versionId={}&projectId={}'.format(VERSION_ID, PROJECT_ID)

        # CANONICAL PATH (Http Method & Relative Path & Query String)

        CANONICAL_PATH = 'GET&/public/rest/api/1.0/cycles/search&' + 'projectId=' + str(
            PROJECT_ID) + '&versionId=' + str(
            VERSION_ID)

        # TOKEN HEADER: to generate jwt token
        payload_token = {
            'sub': USER,
            'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
            'iss': self.access_key,
            'exp': int(time.time()) + JWT_EXPIRE,
            'iat': int(time.time())
        }

        # GENERATE TOKEN
        token = jwt.encode(payload_token, self.secret_key, algorithm='HS256').strip().decode('utf-8')

        # REQUEST HEADER: to authenticate and authorize api
        headers = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'text/plain',
            'zapiAccessKey': self.access_key
        }

        raw_result = requests.get(self.Zephyrurl + RELATIVE_PATH, headers=headers)

        #print("get cycle is", raw_result.text)
        # JSON RESPONSE: convert response to JSON
        json_result = json.loads(raw_result.text)
        for json_val in json_result:
            #print(json_val)
            if json_val['name'] == CYCLE_NAME:
                cycle_id = json_val['id']
        return cycle_id

    def FetchExecutionIdAndIssue_Id(self,PROJECT_ID,VERSION_ID,cycle_id):
        RELATIVE_PATH = '/public/rest/api/1.0/executions/search/cycle/{}?versionId={}&projectId={}'.format(cycle_id,
                                                                                                           VERSION_ID,
                                                                                                           PROJECT_ID)

        CANONICAL_PATH = 'GET&/public/rest/api/1.0/executions/search/cycle/' + cycle_id + '&' + 'projectId=' + str(
            PROJECT_ID) + '&versionId=' + str(VERSION_ID)

        # TOKEN HEADER: to generate jwt token
        payload_token2 = {
            'sub': USER,
            'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
            'iss': self.access_key,
            'exp': int(time.time()) + JWT_EXPIRE,
            'iat': int(time.time())
        }

        # GENERATE TOKEN
        token2 = jwt.encode(payload_token2, self.secret_key, algorithm='HS256').strip().decode('utf-8')

        # REQUEST HEADER: to authenticate and authorize api
        headers2 = {
            'Authorization': 'JWT ' + token2,
            'Content-Type': 'text/plain',
            'zapiAccessKey': self.access_key
        }
        result2 = requests.get(self.Zephyrurl + RELATIVE_PATH, headers=headers2)

        test_details = {}
        test_cases_available = []
        # JSON RESPONSE: convert response to JSON
        json_result2 = json.loads(result2.text)
        #print("fetch list of all cycles", json_result2)
        for json_val in json_result2['searchObjectList']:
            test_details['issueId'] = json_val['execution']['issueId']
            test_details['executionId'] = json_val['execution']['id']
            test_cases_available.append(test_details.copy())
            # PRINT RESPONSE: pretty print with 4 indent
        #print("issueis \n", test_cases_available)
        return test_cases_available

    def create_token(self, username, password, platformurl):
        url = '{}/v1/auth'.format(platformurl)

        response = requests.post(url, headers={'Content-Type': 'application/json'},
                                 json={'username': username, 'password': password, }, verify=False)

        if response.status_code != 200:
            print('Aiq token generation  API status code => {}, response =>{} '.format(response.status_code,
                                                                                       response.text))

        return json.loads(response.text)['token']


    def execution_ID(self, gentoken, platform_url, TestsuiteId,TestcaseId):
        url1 = '{}/v1/jobs/{}/2/get_executions'.format(platform_url,TestsuiteId)
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
        job = res['jobs'][0]
        executionId = ''
        for task in job['etrs']['tasks']:
            TestcaseId=int(TestcaseId)
            if task['testcaseId'] == TestcaseId:
                executionId=task['executionId']
        return executionId

    def fetchIterationstatus(self,gentoken,platformurl,Executionid):
        url = "{}/v1/testexecutions/{}/getexecution".format(platformurl,Executionid)
        print("Execution id", url)
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + gentoken
        }
        #print("reached after payload")
        response = requests.request("GET", url, headers=headers, data=payload)
        assert (response.status_code == 200), "error:Message ITERATION_RESULT{} ".format(response.text)
        #print("after response")
        finalresp = json.loads(response.text)
        #print(finalresp)
        resultData = finalresp['resultData']
        IterationStatus = []
        for i in resultData:
            resultData1 = (i['resultData'])
            ##print("Result of Iteration",resultData1)
            if resultData1:
                for j in resultData1["iterationResult"]:
                    iterationResult = (resultData1["iterationResult"])
                    #print(iterationResult)
                for k in iterationResult:
                    IterationStatus.append(k["is_success"])
                    #print(k["is_success"])
                #print(IterationStatus)
        return IterationStatus

    def UpdateTestResults(self,execution_id,issue_id,PROJECT_ID,VERSION_ID,cycle_id,Status):

        RELATIVE_PATH = '/public/rest/api/1.0/execution/{}?issueId={}&projectId=10006'.format(execution_id, issue_id)

        CANONICAL_PATH = 'PUT&/public/rest/api/1.0/execution/' + execution_id + '&' + 'issueId=' + str(
            issue_id) + '&projectId=' + str(PROJECT_ID)

        if Status == True:
            id=1
        else:
            id=2

        # TOKEN HEADER: to generate jwt token
        payload_token2 = {
            'sub': USER,
            'qsh': hashlib.sha256(CANONICAL_PATH.encode('utf-8')).hexdigest(),
            'iss': self.access_key,
            'exp': int(time.time()) + JWT_EXPIRE,
            'iat': int(time.time())
        }

        # GENERATE TOKEN
        token2 = jwt.encode(payload_token2, self.secret_key, algorithm='HS256').strip().decode('utf-8')

        # REQUEST HEADER: to authenticate and authorize api
        headers2 = {
            'Authorization': 'JWT ' + token2,
            'Content-Type': 'application/json',
            'zapiAccessKey': self.access_key
        }
        payload = {
            "cycleId": cycle_id,
            "id": execution_id,
            "issueId": issue_id,
            "projectId": PROJECT_ID,
            "status": {
                "id": id
            },
            "versionId": VERSION_ID
        }
        result2 = requests.put(self.Zephyrurl + RELATIVE_PATH, headers=headers2, json=payload)
        print(result2.status_code)

#### Main #######
    def run(self):
        csv = self.read_csv(self.csvpath)
        PROJECT_NAME=csv[3]
        RELEASE_NAME=csv[2]
        CYCLE_NAME=csv[4]
        TestsuiteId=csv[0]
        TestcaseId=csv[1]
        #print(PROJECT_NAME,RELEASE_NAME,CYCLE_NAME)

        PROJECT_ID,VERSION_ID=self.FetchReleaseAndProjectId(PROJECT_NAME,RELEASE_NAME)
        #print(PROJECT_ID,VERSION_ID)
        Cyc_id=self.fetchCycle_Id(PROJECT_ID,VERSION_ID,CYCLE_NAME)
        cycle_id=Cyc_id
        Iss_id = self.FetchExecutionIdAndIssue_Id(PROJECT_ID,VERSION_ID,cycle_id)



        gentoken = self.create_token(self.username,self.password,self.platformurl)

        #print(gentoken)

        Executionid=self.execution_ID(gentoken,self.platformurl,TestsuiteId,TestcaseId)
        #print(Executionid)

        IterationResult=self.fetchIterationstatus(gentoken,self.platformurl,Executionid)
        Issueid = Iss_id
        print("IterationResult",IterationResult)
        print("Iss_id", Iss_id)
        Iterationlength =len(IterationResult)
        TestcasesLenInZephyr=len(Iss_id)
        if Iterationlength == TestcasesLenInZephyr:
            for i in range(Iterationlength):
                issue_id=Issueid[i]['issueId']
                execution_id= Issueid[i]['executionId']
                Status=IterationResult[i]
                self.UpdateTestResults(execution_id,issue_id,PROJECT_ID,VERSION_ID,cycle_id,Status)

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-AIQ_url", "--platformurl", type=str,
                        help="Please provide autonomiq server url")

    parser.add_argument("-AIQ_user", "--username", type=str,
                        help="Please provide Autonomiq username", default='appuser')

    parser.add_argument("-AIQ_pass", "--password", type=str,
                        help="Please provide Autonomiq password", default='app123')

    parser.add_argument("-Zephyre_Accountid", "--account_id", type=str,
                        help="Please provide Zephyre AccountId")

    parser.add_argument("-Zephyre_accesskey", "--access_key", type=str,
                        help="Please provide Zephyre accessKey")

    parser.add_argument("-Zephyre_secretkey", "--secret_key", type=str,
                        help="Please provide Zephyre secretkey")

    parser.add_argument("-csvpath", "--csvpath", type=str,
                        help="Please provide Zephyre csvpath")

    parser.add_argument("-Zephyrebaseurl", "--Zephyrurl", type=str,
                        help="Please provide Zephyr server url")


    args = parser.parse_args()
    return args.__dict__

if __name__ == '__main__':

   main(argument_parser()).run()