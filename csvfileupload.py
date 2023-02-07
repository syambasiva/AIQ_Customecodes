import csv

def read_csv11(csvpath):
    reader = csv.reader(open(csvpath))
    result = {}
    first_row = next(reader)
    for row in reader:
            key = row[0]
            if key in result:
                pass
            result[key] = row[1:]
    return result

def read_csv(csvpath):
    reader = csv.reader(open(csvpath))
    result = {}
    result1 = {}
    first_row = next(reader)
    for row in reader:
        key = row[0]
        val = row[5]
        if(val =='Yes'):
           if key in result:
            print(key)
            pass
           result[key] = row[1:]

        if (val == 'No'):
            if key in result:
                print(key)
                pass
            result1[key] = row[1:]

    return result,result1
    print(result)
    print(result1)