import os

def ID(input1,input2,input3):
  str2=''
  dictionary=dict(subString.split("=") for subString in input1.split(";"))
  for i in range(0,int(input2)+1):
    if i==input2:
      str2+=input3[input2]

  for name,id in dictionary.items():
    if name==str2:
      return id

#dict_data='''Ivana Molnárová Dubcová =ID;
 # Pedro Delicado =PD;
  #Montserrat Dominguez =MD''';

dict_data={"Ivana Molnárová Dubcová": "ID", "Pedro Delicado": "PD", "Montserrat Dominguez": "MD"}
iteration_count=0;
str1=['Ivana Molnárová Dubcová', 'Pedro Delicado', 'Montserrat Dominguez'];


fetchvalue = str1[iteration_count]
for key, values in dict_data.items():
  if key == fetchvalue:
    print(values)


#a=ID(dict_data,iteration_count,str1)
#print(a)


