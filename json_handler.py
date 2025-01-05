import json

# Function to append or update data to a JSON file
def update_json(new_data, update: bool, filename='tasks.json'):
    with open(filename, "r+") as outfile:

        # Load existing data
        file_data = json.load(outfile)

        # Check if the file can be updated or appended to
        if update is True:
            for key in new_data:
                if key not in file_data:
                    return False
        elif update is False:
            for key in new_data:
                if key in file_data:
                    return False

        # Append the new data
        file_data.update(new_data)

        # Move file pointer to the beginning and write the updated JSON
        outfile.seek(0)
        json.dump(file_data, outfile, indent=4)
        # Truncate file to avoid leftover characters
        outfile.truncate()

    return True

def write_json(new_data, filename="tasks.json"):
    #Over write existing file with new data
    with open(filename, 'w') as outfile:
        json.dump(new_data, outfile)

    return True

def read_json(key, filename="tasks.json"):
    #Read the value of a specifi key
    with open(filename, "r") as outfile:
        file = json.load(outfile)

        return file.get(key, None)
    
def delete_json(key, filename="tasks.json"):
    #Delete on row
    with open(filename, "r+") as outfile:
        file = json.load(outfile)

        if key in file:
            del file[key]
    
            outfile.seek(0)
            #Update the content
            json.dump(file, outfile, indent=4)
            outfile.truncate()

            return True
        else:
            return False