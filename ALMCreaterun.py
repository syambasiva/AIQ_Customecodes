import requests
import xmltodict
from datetime import date
from datetime import datetime
from pytz import timezone


def create_run(AlmBaseUrl, ALM_cookie, status, value,ExecutionIds,Testcategory):

    today = date.today()

    now = datetime.now()
    fmt = "%H-%M-%S"
    now_time = datetime.now(timezone('US/Eastern'))

    if status == "SUCCESS":
        status = "Passed"
    else:
        status = "Failed"

    url = "{}/qcbin/rest/domains/INVACARE/projects/SKYDIVE/runs".format(AlmBaseUrl)

    payload = "<Entity Type='run'>\r\n <Fields>\r\n  <Field Name='name'><Value>Fast_Run_{}_{}</Value></Field>\r\n " \
              "<Field Name='test-instance'><Value>1</Value></Field>\r\n  <Field Name='cycle-id'><Value>{}</Value>" \
              "</Field>\r\n <Field Name='test-id'><Value>{}</Value></Field>\r\n <Field Name='subtype-id'>" \
              "<Value>hp.qc.run.MANUAL</Value></Field>\r\n <Field Name='status'><Value>{}</Value></Field>\r\n " \
              "<Field Name=\"testcycl-id\"><Value>{}</Value></Field>\r\n " \
              "<Field Name='owner'><Value>aiq_automation</Value></Field>\r\n " \
              "<Field Name='user-template-07'><Value>Draft</Value></Field>"\
              "<Field Name='user-template-10'><Value>Y</Value></Field>"\
              "<Field Name='user-template-08'><Value>aiq_automation</Value></Field>" \
              "<Field Name='user-01'><Value>{}</Value></Field></Fields>\r\n</Entity>".format(now.strftime("%m-%d"),now_time.strftime(fmt),
                                                                                                       value[0],
                                                                                                       value[1], status,
                                                                                                       value[2],ExecutionIds)

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
