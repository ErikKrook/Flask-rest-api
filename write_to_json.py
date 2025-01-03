import json

file_path = 'tasks.json'

tasks = {
    "1":"Handla",
    "2":"Diska",
    "3":"Clean",
    "4":"Eat"
}

def json_file(file_path, dict):

    with open(file_path, 'w') as outfile:
        json.dump(dict, outfile)

    return print("Done")

if __name__ == '__main__':
    json_file(file_path, tasks)