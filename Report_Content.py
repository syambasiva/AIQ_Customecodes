import codecs
from lxml import etree

from bs4 import BeautifulSoup

status = []

file = codecs.open("test.html",
                   "r", "utf-8")
c = file.read()
soup = BeautifulSoup(c, 'html.parser')
print(soup)
PrintData = soup.findAll('div', {'class': 'description__text'})

print(PrintData)


dom = etree.HTML(str(soup))
val = dom.xpath('//span[text()="print" or text() ="Print"]/parent::div//preceding-sibling::div/span')

for i in val:
    status.append(i.text)
# print(status)
# for j in status:


final_list = []
for i in PrintData:
    values = i.findAll('p')
    if ((values[0].text == "Teststep : Print") or (values[0].text == "Teststep : print")):
        text1 = values[1].text.split(':')[1]
        split_data = text1.split('|')
        first_message = split_data[0]
        second_message = split_data[1]
        final_list.append(split_data)
##print(final_list)

final_list1=[]
for i in range(len(status)):
    if status[i] == "SUCCESS":
        var_msg = final_list[i][0]
    else:
        status[i] == "Not Executed"
        var_msg = final_list[i][0]
    ss = dict(status=status[i], message=var_msg)
    final_list1.append(ss)
i=3
print(final_list1)
div=len(final_list1)




