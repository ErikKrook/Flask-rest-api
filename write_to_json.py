import json
import os

file_path = 'task.json'

tasks = {
    "1":"Handla",
    "2":"Diska",
    "3":"Städa",
    "4":"Äta"
}

def json_file(dict):

    json_object =  json.dumps(dict, indent=4)

    with open('tasks.json', 'w') as outfile:
        outfile.write(json_object)

    return print("Done")

if __name__ == '__main__':
    json_file(tasks)