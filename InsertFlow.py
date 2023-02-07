import argparse
import logging

import requests
import json



class UpdateInsertFlow:
    def __init__(self, kwargs):
        logger = logging
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.platformurl = kwargs.get('platformurl')
        self.projectname = kwargs.get('projectname')
        self.flowname = kwargs.get('flowname')
        self.platformurl_1 = kwargs.get('platformurl_1')
        self.username_1 = kwargs.get('username_1')
        self.password_1 = kwargs.get('password_1')
        self.projectname_1 = kwargs.get('projectname_1')
        self.logger = logger

    def run(self):
        try:

            self.fetchAccount(self.username,self.password,self.platformurl,self.projectname,self.flowname,
                                self.platformurl_1,self.username_1,self.password_1,self.projectname_1,self.logger)


        except Exception as error:
            print(error)

    # Base site Authentication and Userid
    def fetchAccount(self, username, password, platformurl, projectname, flowname,
                     platformurl_1, username_1, password_1, projectname_1, logger):
        url = "{}/v1/auth".format(platformurl)
        print(url)

        payload = json.dumps({
            "username": username,
            "password": password
        })
        headers = {
            'Authorization': 'Basic aW5kaHVtYXRoaTphaXFAMTIz',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        resp11 = response.text
        j = json.loads(resp11)
        userid1 = j['userAccount']
        token1 = j['token']
        print("userid 1:")
        print(userid1)
        logging.basicConfig(filename="std.log",filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info('Authentication done')

        projectname1 = projectname

        url = "{}/v1/getprojects".format(platformurl)

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'content-type': 'multipart/form-data',
            'Authorization': 'Bearer ' + token1,
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        resp12 = response.text
        k = json.loads(resp12)
        for i in k:
            if i['projectName'] == projectname1:
                projectid1 = (i['projectId'])
        print("projectid1:")
        print(projectid1)

        # Base site Flow Details
        url = "{}/blocks/getAll/{}/{}".format(platformurl,userid1, projectid1)

        flowname_1= flowname
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + token1,
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        resp13 = response.text
        l = json.loads(resp13)

        for i in l:
            if (i['name']) == flowname_1:
                flowsteps1 = (i)
        print("Steps1:")
        print(flowsteps1)

        # Required site Authentication and Userid
        #url = "https://delltech.autonomiq.ai/platform/v1/auth"
        url = "{}/v1/auth".format(platformurl_1)

        payload = json.dumps({
            "username": username_1,
            "password": password_1
        })
        headers = {
            'Authorization': 'Basic ZGVsbGFkbWluOmRlbGxhZG1pbjEyMzQ=',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        resp21 = response.text
        m = json.loads(resp21)
        userid2 = m['userAccount']
        token2 = m['token']
        print("userid 2:")
        print(userid2)

        # Required Project Details
        projectname2 = projectname_1

        url = "{}/v1/getprojects".format(platformurl_1)

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'content-type': 'multipart/form-data',
            'Authorization': 'Bearer ' + token2,
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        resp22 = response.text
        n = json.loads(resp22)

        for i in n:
            if i['projectName'] == projectname2:
                projectid2 = (i['projectId'])
        print("projectid2:")
        print(projectid2)

        # edit Json
        insert_object = json.dumps(flowsteps1)
        insert_object = json.loads(insert_object)
        insert_object["accountId"] = userid2
        insert_object["projectId"] = projectid2

        print(insert_object)
        print(type(insert_object))
        # Required site Flow Details
        url = "{}/blocks/getAll/{}/{}".format(platformurl_1,userid2, projectid2)

        payload = {}
        headers = {
            'Authorization': 'Bearer ' + token2,
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        resp23 = response.text
        o = json.loads(resp23)

        for i in o:
            if (i['name']) == flowname:
                flowsteps2 = (i)
                print("Steps2:")
                print(flowsteps2)

                # edit Json
                json_object2 = json.dumps(flowsteps2)
                json_object2 = json.loads(json_object2)
                accId = json_object2["accountId"]
                projId = json_object2["projectId"]
                flowname_del = json_object2["name"]
                delete_object = {"account_id": accId, "project_id": projId, "name": flowname_del}
                print(type(delete_object))

                # delete exisiting
                url = "{}/v1/blocks/delete".format(platformurl_1)

                payload = json.dumps(delete_object)
                headers = {
                    'Authorization': 'Bearer ' + token2,
                    'Content-Type': 'application/json'
                }
                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)

                # Final insertion
                url = "{}/blocks/insert".format(platformurl_1)

                payload = json.dumps(insert_object)
                headers = {
                    'Authorization': 'Bearer ' + token2,
                    'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)





def argument_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-AIQ_url", "--platformurl", type=str,
                        help="Please provide autonomiq server url")

    parser.add_argument("-AIQ_user", "--username", type=str,
                        help="Please provide Autonomiq username", default='appuser')

    parser.add_argument("-AIQ_pass", "--password", type=str,
                        help="Please provide Autonomiq password", default='app123')

    parser.add_argument("-AIQ_projectname", "--projectname", type=str,
                        help="Please provide Autonomiq projectname", default='test')

    parser.add_argument("-AIQ_flowname", "--flowname", type=str,
                        help="Please provide Autonomiq flowname", default='test')

    parser.add_argument("-AIQ_url_1", "--platformurl_1", type=str,
                        help="Please provide autonomiq server url_1")

    parser.add_argument("-AIQ_user_1", "--username_1", type=str,
                        help="Please provide Autonomiq username", default='appuser')

    parser.add_argument("-AIQ_pass_1", "--password_1", type=str,
                        help="Please provide Autonomiq password", default='app123')

    parser.add_argument("-AIQ_projectname_1", "--projectname_1", type=str,
                        help="Please provide Autonomiq projectname_1", default='test')

    args = parser.parse_args()
    return args.__dict__


if __name__ == '__main__':
    FromURL = 'https://client-demo.internal.autonomiq.ai/platform'

    Fromusername = 'indhumathi'

    FromPassword = 'aiq@123'

    FromProjectName = 'Sample_Testcases_new'

    Fromflowname = 'ExampleFlow'

    ToURL = 'https://delltech.autonomiq.ai/platform'

    ToUsername = 'delladmin'

    ToPassword = 'delladmin1234'

    ToprojectName = 'sample_tc'
    UpdateInsertFlow(argument_parser()).run()