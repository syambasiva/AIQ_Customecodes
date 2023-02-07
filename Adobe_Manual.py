import requests
import json
import xlsxwriter

workbook = xlsxwriter.Workbook('manualFailureReport.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

val= '[]';
values =values = json.loads(val.replace("'", '"'))
Date='2023-01-19';
iter_val=1;

############### Test data ################

TestExecutionName=['1_Schemas: Create (Individual) Profile Schema_Updated_1_UI Quality Automation Test Results',
'2_Schemas: Experience Event Schema_Updated_Nike_Workflows_UI Quality Automation Test Results',
'3_Datasets: Create dataset from schema_Nike_Workflows_UI Quality Automation Test Results',
'4_Segments: Create a Standard Audience_Nike_Workflows_UI Quality Automation Test Results',
'5_Destinations or Activation: Create a Amazon S3 Destination and activate a Segment to it_Nike_Workflows_UI Quality Automation Test Results',
'7_Segments or Activation: Activate Segments From Segment Page : Export Incremental Files_Nike_Workflows_UI Quality Automation Test Results',
'8_Source: Ingest data from S3 source connector_UI Quality Automation Test Results',
'9_Profiles: Create merge policy_UI Quality Automation Test Results',
'10_Profiles: Identify a namespace, look up a profile_UI Quality Automation Test Results',
'11_Dashboards: Confirm that standard widgets load properly on all dashboards_UI Quality Automation Test Results',
'12_Data Governance: Create a policy_UI Quality Automation Test Results',
'13_Data Governance: Schema Labeling_UI Quality Automation Test Results',
'14_Data Governance: Create a label_UI Quality Automation Test Results',
'15_Schemas: Field Search_UI Quality Automation Test Results',
'16_Schemas: Switch Class_UI Quality Automation Test Results',
'17_Schemas: Create schema from custom class, add field group and extend further_UI Quality Automation Test Results',
'18_Monitoring: Confirm Monitoring pages load properly_UI Quality Automation Test Results',
'20_Segments_ Left Rail – Verify Attributes, Events, Audiences are clickable and have expected data_label for each in the initial folder_UI Quality Automation Test Results',
'22_Segments_Verify successful deletion of a rule_UI Quality Automation Test Results',
'23_Data Governance: Create a consent policy_UI Quality Automation Test Results',
'24_Segments_ Verify Forming A Group_Nested Container Scenarios_UI Quality Automation Test Results',
'25_Segments_ Verify Successful Deletion Of a (sub)Container_UI Quality Automation Test Results']

value=[266,134,73,102,75,77,135,299,300,301,298,519,351,372,374,373,375,441,443,444,477,499]

Values_List=[]

Iteration=int(iter_val);

#################### Values ######################


headings = ['TESTCASE NAME','SUCCESS','FAILURE','Execution_ID']

##headings = ['Number', 'Batch 1', 'Batch 2']

url = "https://adobe.autonomiq.ai/platform/v1/auth"

payload = json.dumps({
  "username": "adobeadmin",
  "password": "Adobeadmin@123"
})

headers = {
  'Authorization': 'Basic YWRvYmVhZG1pbjpBZG9iZWFkbWluQDEyMw==',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

j = json.loads(response.text)
token = j['token']

def sum_lists(*args):
  return list(map(sum, zip(*args)))



count=len(value);


if(Iteration==1):
    ##TestExecutionName = []
    Failurecount = []
    Successcount = []
    ExecutionId_list = []

    for i in value:
        url = "https://adobe.autonomiq.ai/platform/testScriptExecutions/2/7/{}/-1/0/executions".format(i)

        payload={}
        headers = {
                'Content-Type': 'application/json',
                'content-type': 'multipart/form-data',
                'Authorization': 'Bearer {}'.format(token)
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        L = json.loads(response.text)
        ExecutionCount=L['tasks']

        ##TestExecutionName.append(ExecutionCount[0]['executionName'])

        if (ExecutionCount[0]['executionStatus'] == "INPROGRESS"):
            Executionvalue = ExecutionCount[1]['executionId']
        else:
            Executionvalue = ExecutionCount[0]['executionId']

        ExecutionId_list.append(Executionvalue)

        failurecount=0;
        successcount=0;
        for i in ExecutionCount:
            date1 = i['initiatedOn']
            date2 = date1.split('T')[0]
            if (Date == date2):
                if (i['executionStatus'] == "ERROR"):
                    failurecount = failurecount + 1;
                if (i['executionStatus'] == "SUCCESS"):
                    successcount = successcount + 1;

        Failurecount.append(failurecount)
        Successcount.append(successcount)

    data = [
        TestExecutionName,
        Successcount,
        Failurecount,
        ExecutionId_list
    ]

    worksheet.write_row('A1', headings, bold)
    worksheet.write_column('A2',data[0])
    worksheet.write_column('B2',data[1])
    worksheet.write_column('C2',data[2])
    worksheet.write_column('D2',data[3])




    chart1 = workbook.add_chart({'type': 'bar'})


    chart1.add_series({
        'name':       ['Sheet1', 0, 2],
        'categories': ['Sheet1', 1, 0, count, 0],
        'values':     ['Sheet1', 1, 2, count, 2],
    })

    chart1.add_series({
        'name':       ['Sheet1', 0, 1],
        'categories': ['Sheet1', 1, 0, count, 0],
        'values':     ['Sheet1', 1, 1, count, 1],
    })

    chart1.set_title({'name': 'Failure data analysis'})

    chart1.set_x_axis({'name': 'Failure count'})

    chart1.set_y_axis({'name': 'Testcase Names(mm)'})

    chart1.set_style(12)

    worksheet.insert_chart('G2', chart1)

    workbook.close()

    Values_List.append(json.dumps(Successcount))
    Values_List.append(json.dumps(Failurecount))
    Values_List.append(json.dumps(ExecutionId_list))
    print(Values_List)

if(Iteration!=1):

    New_Values_List=[]

    New_TestExecutionName = ['1_Schemas: Create (Individual) Profile Schema_Updated_1_UI Quality Automation Test Results',
                        '2_Schemas: Experience Event Schema_Updated_Nike_Workflows_UI Quality Automation Test Results',
                        '3_Datasets: Create dataset from schema_Nike_Workflows_UI Quality Automation Test Results',
                        '4_Segments: Create a Standard Audience_Nike_Workflows_UI Quality Automation Test Results',
                        '5_Destinations or Activation: Create a Amazon S3 Destination and activate a Segment to it_Nike_Workflows_UI Quality Automation Test Results',
                        '7_Segments or Activation: Activate Segments From Segment Page : Export Incremental Files_Nike_Workflows_UI Quality Automation Test Results',
                        '8_Source: Ingest data from S3 source connector_UI Quality Automation Test Results',
                        '9_Profiles: Create merge policy_UI Quality Automation Test Results',
                        '10_Profiles: Identify a namespace, look up a profile_UI Quality Automation Test Results',
                        '11_Dashboards: Confirm that standard widgets load properly on all dashboards_UI Quality Automation Test Results',
                        '12_Data Governance: Create a policy_UI Quality Automation Test Results',
                        '13_Data Governance: Schema Labeling_UI Quality Automation Test Results',
                        '14_Data Governance: Create a label_UI Quality Automation Test Results',
                        '15_Schemas: Field Search_UI Quality Automation Test Results',
                        '16_Schemas: Switch Class_UI Quality Automation Test Results',
                        '17_Schemas: Create schema from custom class, add field group and extend further_UI Quality Automation Test Results',
                        '18_Monitoring: Confirm Monitoring pages load properly_UI Quality Automation Test Results',
                        '20_Segments_ Left Rail – Verify Attributes, Events, Audiences are clickable and have expected data_label for each in the initial folder_UI Quality Automation Test Results',
                        '22_Segments_Verify successful deletion of a rule_UI Quality Automation Test Results',
                        '23_Data Governance: Create a consent policy_UI Quality Automation Test Results',
                        '24_Segments_ Verify Forming A Group_Nested Container Scenarios_UI Quality Automation Test Results',
                        '25_Segments_ Verify Successful Deletion Of a (sub)Container_UI Quality Automation Test Results']
    SuccesscountITR_1 =  json.loads(values[0]);
    FailurecountITR_1 = json.loads(values[1]);
    New_ExecutionId_list = json.loads(values[2]);

    ##print("old Values")
    ##print(SuccesscountITR_1)
    ##print(type(SuccesscountITR_1))

    New_ExecutionId_list1=[]
    New_SuccesscountITR_1=[]
    New_FailurecountITR_1=[]

    for i in range(0, count):
        url = "https://adobe.autonomiq.ai/platform/testScriptExecutions/2/4/{}/-1/0/executions".format(value[i])
        e1=New_ExecutionId_list[i]
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'content-type': 'multipart/form-data',
            'Authorization': 'Bearer {}'.format(token)
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        L = json.loads(response.text)
        ExecutionCount = L['tasks']

        if (ExecutionCount[0]['executionStatus'] == "INPROGRESS"):
            Executionvalue = ExecutionCount[1]['executionId']
        else:
            Executionvalue = ExecutionCount[0]['executionId']

        New_ExecutionId_list1.append(Executionvalue)

        failurecount = 0;
        successcount = 0;
        for i in ExecutionCount:
            if (i['executionId'] == e1):
                ##print(e1.value)
                ##print(i['executionId'])
                ##print("inside loop")
                break;
            date1 = i['initiatedOn']
            date2 = date1.split('T')[0]
            if (Date == date2):
                ##print(i['executionId'])
                if (i['executionStatus'] == "ERROR"):
                    failurecount = failurecount + 1;
                if (i['executionStatus'] == "SUCCESS"):
                    successcount = successcount + 1;

        New_FailurecountITR_1.append(failurecount)
        New_SuccesscountITR_1.append(successcount)

    Final_Failure = sum_lists(FailurecountITR_1, New_FailurecountITR_1)
    Final_Success = sum_lists(SuccesscountITR_1, New_SuccesscountITR_1)
    data = [
        New_TestExecutionName,
        Final_Success,
        Final_Failure,
        New_ExecutionId_list1
    ]
    worksheet.write_row('A1', headings, bold)
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3])

    workbook.close()
    New_Values_List.append(json.dumps(Final_Success))
    New_Values_List.append(json.dumps(Final_Failure))
    New_Values_List.append(json.dumps(New_ExecutionId_list1))
    print(New_Values_List)









