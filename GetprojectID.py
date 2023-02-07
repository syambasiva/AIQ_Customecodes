import json
def splitcode():
    c= "a|b|c"
    value=  c.split("|")
    values=value[::-1]
    print(values)
    result =  list()
    for i in values:
        result.append({"name": i})
        json_string = json.dumps(result)
    return json_string
c= splitcode()
print(c)