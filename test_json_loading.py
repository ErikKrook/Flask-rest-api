import unittest
from append_to_json import update_json
import json

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_tasks.json'
        with open(self.test_file, 'w') as file:
            json.dump({"1": "Task1"}, file)

    def tearDown(self):
        import os
        os.remove(self.test_file)

    def test_append(self):
        # Test to append a value
        data = {"2":"Test append"}
        response = update_json(data, 0, self.test_file)
        self.assertEqual(response, True)
    
    def test_append_fail(self):
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
        data = {"4":"Test Update"}
        response = update_json(data, 1, self.test_file)
        self.assertEqual(response, False)
        


if "__main__" == __name__:
    unittest.main()

