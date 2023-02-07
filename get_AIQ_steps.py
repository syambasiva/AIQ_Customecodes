import argparse
import json
import requests
import re
from multiprocessing.dummy import Pool as ThreadPool

import csv
import logging


def get_header(token):
    return {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Authorization': "Bearer {}".format(token),
        'cache-control': "no-cache",
    }

def get_request(url, params=None, headers=None):
    rsp = requests.get(url, json=params, headers=headers, verify=False)
    assert rsp.status_code == 200, 'API => {}, Response => {}'.format(url, rsp.text)
    return rsp


def get_test_case_info(gentoken, platformurl, test_case_id):
    url = "{}/v1/testexecutions/{}/getexecution".format(platformurl, test_case_id)
    ##print("url of aiq steps",url)

    response = get_request(url, headers=get_header(gentoken))
    ##print("get testcase info",response)

    if response.status_code != 200:
        print('Get testcase info API status code => {}, response =>{} '.format(response.status_code,
                                                                               response.text))
    return json.loads(response.text)

def final_result(gentoken,platformurl,test_case_id):
        final_list = []
        try:
            a = get_test_case_info(gentoken,platformurl,test_case_id)
            b = json.loads(a['Steps'])
            ##print("check step values")
            start, end, status, count = (0, 0, 5, 0)
            first_message, second_message, block_name = ('Not processed', 'Not processed', '')
            skip = False
            # [{},{},{},{},{}]
            final_list = []
            var_msg = ''
            for i in b:
               if re.findall(r"run\s+\${(.*)}", i['instr'], re.IGNORECASE) and i['isBlockStep']== True:
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

