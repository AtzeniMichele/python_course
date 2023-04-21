import json

def json_handler(file_name):
    dictionary = dict()
    with open('json_files/' + file_name + '.json','r') as file:
        for line in file:
            p = json.loads(line)
            dictionary[p['name']] = p
    return dictionary

def json_effectiveness_handler(file_name):
    dictionary = dict()
    i = 0
    with open('json_files/' + file_name + '.json','r') as file:
        for line in file:
            p = json.loads(line)
            dictionary[i] = p
            i = i+1
    return dictionary
