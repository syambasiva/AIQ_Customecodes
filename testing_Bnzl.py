
import json

import xlrd
from xlutils.copy import copy


list = json.loads(aiq_1.replace("'", '"'))
column=aiq_2;

filename=aiq_3;

col=int(column)
length=len(list)

print(len(list))
print(filename)
print(col)

for i in range(length):
    print(list[i],":",i)
    rb = xlrd.open_workbook(filename, "rb")

    wb = copy(rb)

    w_sheet = wb.get_sheet(0)

    w_sheet.write(i+1,col,list[i])

    wb.save(filename)
