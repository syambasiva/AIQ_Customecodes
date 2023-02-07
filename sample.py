import json

def splitcode():
    c= "mohini|raju|John"
    value=c.split("|")
    result = []
    for i in value:
        result.append({"name": i,"DOB":i})
        json_string = json.dumps(result)
    return json_string

c= splitcode()
print(c)

