import unittest
from json_handler import update_json, read_json, delete_json
import json

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_tasks.json'
        with open(self.test_file, 'w') as file:
            json.dump({"1": "Task1", "4": "Task4", "5":"Task5"}, file)

    def tearDown(self):
        import os
        os.remove(self.test_file)

    def test_append(self):
        # Test to append a value
        data = {"2":"Test append"}
        response = update_json(data, 0, self.test_file)
        self.assertEqual(response, True)
    
    def test_append_already_existing_key(self):
        # Test to append a value where a key already exists
        data = {"1":"Test append"}
        response = update_json(data, 0, self.test_file)
        self.assertEqual(response, False)

    def test_update(self):
        # Test to update a value
        data = {"1":"Test Update"}
        response = update_json(data, 1, self.test_file)
        self.assertEqual(response, True)

    def test_update_non_existing_key(self):
        # Test to update an nonexisting value
        data = {"3":"Test Update"}
        response = update_json(data, 1, self.test_file)
        self.assertEqual(response, False)

    def test_read(self):
        # Test reading a value
        response = read_json("4", "test_tasks.json")
        self.assertEqual(response, "Task4")

    def test_read_non_existing_key(self):
        # Test reading a non existing value
        response = read_json("3", "test_tasks.json")
        self.assertEqual(response, None)

    def test_delete(self):
        # Test to delete on row
        response = delete_json("5", "test_tasks.json")
        self.assertEqual(response, True)

    def test_delete_non_existing_key(self):
        # Test deleting a non existing value
        response = delete_json("3", "test_tasks.json")
        self.assertEqual(response, False)

if "__main__" == __name__:
    unittest.main()

