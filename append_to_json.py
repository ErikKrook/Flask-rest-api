import json

# Function to append data to a JSON file
def update_json(new_data, update, filename='tasks.json'):
    with open(filename, 'r+') as file:

        # Load existing data
        file_data = json.load(file)

        # Check if the file can be updated or appended to
        if update == True:
            for key in new_data:
                if key not in file_data:
                    #print(f"Error key {key} not in use")
                    return False
        elif update == False:
            for key in new_data:
                if key in file_data:
                    #print(f"Error key {key} already in use")
                    return False

        # Append the new data
        file_data.update(new_data)

        # Move file pointer to the beginning and write the updated JSON
        file.seek(0)
        json.dump(file_data, file, indent=4)
        # Truncate file to avoid leftover characters
        file.truncate()

    return True

def write_json(new_data, file_name='tasks.json'):

    #Over write existing file
    with open(file_name, 'w') as outfile:
        json.dump(new_data, outfile)

    return True