import unittest
from json_handler_integration import update_json, read_json, delete_json
import json
import os

class TestFileOperations(unittest.TestCase):
 
    def setUp(self):
        # Path to the test file
        self.test_file = "test_tasks.json"
        
        # Data to be written to the file
        initial_data = {
            "1": "Task1",
            "4": "Task4",
            "5": "Task5"
        }
        
        # Write the data to the file
        with open(self.test_file, "w") as file:
            json.dump(initial_data, file, indent=4)

    def tearDown(self):
        # Remove the test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    

    def test_append(self):
        # Test to append a value
        data = {"2":"Test append"}
        response = update_json(data, 0)
        self.assertEqual(response, True)
    
    def test_append_already_existing_key(self):
        # Test to append a value where a key already exists
        data = {"1":"Test append"}
        response = update_json(data, 0)
        self.assertEqual(response, False)

    def test_update(self):
        # Test to update a value
        data = {"1":"Test Update"}
        response = update_json(data, 1)
        self.assertEqual(response, True)

    def test_update_non_existing_key(self):
        # Test to update an nonexisting value
        data = {"3":"Test Update"}
        response = update_json(data, 1)
        self.assertEqual(response, False)

    def test_read(self):
        # Test reading a value
        response = read_json("4")
        self.assertEqual(response, "Task4")

    def test_read_non_existing_key(self):
        # Test reading a non existing value
        response = read_json("3")
        self.assertEqual(response, None)

    def test_delete(self):
        # Test to delete on row
        response = delete_json("5")
        self.assertEqual(response, True)

    def test_delete_non_existing_key(self):
        # Test deleting a non existing value
        response = delete_json("3")
        self.assertEqual(response, False)

if "__main__" == __name__:
    unittest.main()

