import logging
import requests
import json

def is_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    return True

class ApiTestHandler:

    def __init__(self, base_url, user, password,suiteid,TestcaseId,logger=logging):
        self.base_url = base_url + "/platform"
        self.user = user
        self.passwd = password
        self.token = None
        self.ExecutionId = None
        self.logger = logger
        self.suiteid = suiteid
        self.TestcaseId = TestcaseId


    def get_header(self):
            return {

                'Authorization': "Bearer {}".format(self.token),
            }

    def set_token(self, url="/v1/auth"):
            try:

                resp = self.post_request(url, headers={"Content-Type": "application/json"},
                                         params={"username": self.user, "password": self.passwd}).text

                j = json.loads(resp)

                self.token = j['token']

                self.logger.debug("token: {}".format(self.token))

                self.userId = j['userId']
                self.logger.debug("userId: {}".format(self.userId))

                self.userAccount = j['userAccount']
                self.logger.debug("userAccount: {}".format(self.userAccount))
            except Exception as e:
                self.logger.exception('Failed to generate aiq token, exception {}'.format(e))

    def post_request(self, url, params=None, headers=None, use_json=True):
        full_url = self.base_url + url
        self.logger.debug("full_url: {}".format(full_url))
        self.logger.debug("params: {}".format(params))
        if use_json:
            rsp = requests.post(full_url, json=params, headers=headers, verify=False)
        else:
            rsp = requests.post(full_url, data=params, headers=headers, verify=False)
        if rsp.status_code != 200:
            print('Get testcase info API status code => {}, response =>{} '.format(rsp.status_code,
                                                                                rsp.text))
        return rsp

    def execution_ID(self):
        try:
            print("testcaseid of suite",self.TestcaseId)
            url = "/v1/jobs/{}/2/get_executions".format(self.suiteid)
            rsp = self.get_request(url,headers={"Content-Type": "application/json",'Authorization': 'Bearer ' + self.token})
            res = json.loads(rsp.text)
            job = res['jobs'][0]
            executionId = []
            for task in job['etrs']['tasks']:
                if task['testcaseId'] == self.TestcaseId:
                    executionId.append(task['executionId'])
            print("executionID",executionId)
        except Exception as e:
            self.logger.exception('Failed to fetch Execution ID, exception {}'.format(e))


    def get_request(self,url,headers=None,use_json=True):
        full_url = self.base_url + url
        self.logger.debug("full_url: {}".format(full_url))
        if use_json:
            rsp = requests.get(full_url, headers=headers, verify=False)
            if rsp.status_code != 200:
                print('Get testcase info API status code => {}, response =>{} '.format(rsp.status_code,
                                                                                       rsp.text))
        else:
            rsp = requests.get(full_url, headers=headers, verify=False)
        return rsp

    def get_test_case_info(self, url ="/v1/testexecutions/{}/getexecution".format()):

        response = self.get_request(url, headers=self.get_header())

        if response.status_code != 200:
            print('Get testcase info API status code => {}, response =>{} '.format(response.status_code,
                                                                                   response.text))
        resGetTest = json.loads(response.text)
        return resGetTest








