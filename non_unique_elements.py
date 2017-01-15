# Retain and output non-unique elements in a list

def checkio(data):
    result = []
    for i in data:
        if data.count(i) > 1:
            result.append(i)
    return result
