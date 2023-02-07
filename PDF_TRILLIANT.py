import os
import PyPDF2
import pdfplumber
try:
    import PyPDF2
    import pdfplumber
except ImportError:
    os.system('/usr/bin/python3.6 -m pip install PyPDF2')
    os.system('/usr/bin/python3.6 -m pip install pdfplumber')



def getPDFContent(path,value):
    string1=value
    string1=string1.replace(" ","")
    string1=string1.replace("\n","")
    string1 = string1.replace("'", "")
    #print(string1)
    pdf_file = path
    flag=False
    text=''
    with pdfplumber.open(pdf_file) as pdf:
      for page in pdf.pages:
        text=page.extract_text()
        text=text.replace(" ", "")
        text=text.replace("\n","")
        text = text.replace("'", "")
        #print(text)
        #print("complete string",text,"\n" "aiq_2 string",string1)
        if string1 in text:
            flag=True
            return True

    if flag==False:
      return False


path="/Users/indhumathirajappa/Documents/My codes/Trilliant(NewTeam)/PRSocketGridView.pdf";
input="""1234 Minicloset Slave SQA 1234   Quad Logic MiniCloset-5 Metering Point 12/15/2021 14:15:00 12/15/2021 13:11:58 12/15/2021 13:11:53 kra. 7 156 - 298         10/13/2021 17:03:08          
1234532P 1234532P PRIMESTONE 801054736   Edmi MK32P Cluster 10/18/2021 15:12:18               10/06/2021 15:11:52          
123456789 Prueba_123 PRIMESTONE 1208HD2   Power Measurement ION 7750 07/28/2022 08:01:52               09/28/2022 08:01:35          
12345test PruebasICPI PRIMESTONE 151515   Complant SLD16 09/23/2022 09:05:20               11/23/2022 08:52:18          """
r=input.replace("\n","")
#x=input.split("\n")
#print(x)
y=r.split(" ")
#print(y)
z=list(filter(None,y))
print(z)
#print(len(z))
result=[]
for i in range(0,len(z)):
    c= getPDFContent(path,z[i])
    result.append(c)
print(result)
#print(len(result))
if False in result:
    print("False")
else:
    print("True")