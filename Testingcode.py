import re

import requests
import json


def final_result(b):
    final_list = []
    try:
        #a = self.get_test_case_info(gentoken, platformurl, test_case_id)
        #b = json.loads(a['Steps'])
        # print("steps of print",b)
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
                        #print(k['data'])
                        split_data = k['data'].split('|')
                        first_message = split_data[0]
                        second_message = split_data[1]
                        if k['status'] == '0':
                            var_msg = first_message
                            #print(var_msg)
                        elif k['status'] == '5':
                            var_msg = second_message
                            #print(var_msg)
                        else:
                            var_msg = "Not processed"
                        ss = dict(status=k['status'], message=var_msg)
                        #print(ss)
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
                #print(ss)
                if i['message'] == 'Not processed':
                    return

    except Exception as e:
        print("Error {} ".format(e))
    finally:
        return final_list


url = "http://172.20.4.25/platform/v1/auth"

payload = json.dumps({
  "username": "nagashree",
  "password": "nagashree"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic bmFnYXNocmVlOm5hZ2FzaHJlZQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)
token=json.loads(response.text)['token']
print(token)

import requests

url = "http://172.20.4.25/platform/v1/testexecutions/5134/getexecution"

payload={}
headers = {
  'Authorization': 'Bearer ' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

result=json.loads(response.text)
b = json.loads(result['Steps'])
print("value of b",b)
result=final_result(b)
#print("final result",result)



