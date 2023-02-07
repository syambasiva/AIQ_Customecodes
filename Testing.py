import os
try:
    import zipfile
    import openpyxl
    from pathlib import Path

except ImportError:
    os.system('/usr/bin/python3.6 -m pip install --upgrade pip')
    os.system('/usr/bin/python3.6 -m pip install --upgrade setuptools')
    os.system('/usr/bin/python3.6 -m  pip install zipfile36')
    os.system('/usr/bin/python3.6 -m  pip install openpyxl')



def getExcel():
    filename='./summarized_transactions_report_csv.zip';
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        Extractfile = zip_ref.extractall('./')

    list=[1]
    print(type(list))
    zip = zipfile.ZipFile(filename)
    value= zip.namelist()
    print(zip.namelist()[0])
    list1=[]
    for i in value:
        list1.append(i)
    print(list1)
    Testcase_Execution_status = dict(zip(list,list1))


Excel = getExcel()



