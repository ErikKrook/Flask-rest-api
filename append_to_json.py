import json

# Function to append data to a JSON file
def append_json(new_data, filename='tasks.json'):
    with open(filename, 'r+') as file:

            # Load existing data
        file_data = json.load(file)


        # Append the new data
        file_data.update(new_data)

        # Move file pointer to the beginning and write the updated JSON
        file.seek(0)
        json.dump(file_data, file, indent=4)
        # Truncate file to avoid leftover characters
        file.truncate()

# Python object to be appended
task = {"5": "Walk"}

append_json(task)
