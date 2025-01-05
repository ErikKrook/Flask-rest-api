import unittest
import json
import os

from app_integration import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self): # Create a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True 
        # Path to the test file
        self.test_file = "test_tasks.json"
        
        # Data to be written to the file
        initial_data = {
            "2": "Task2",
            "4": "Task4",
            "7": "Task7",
            "8": "Task8",
            "10": "Task10"
        }
        
        # Write the data to the file
        with open(self.test_file, "w") as file:
            json.dump(initial_data, file, indent=4)

    def tearDown(self):
        # Remove the test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_get_task_not_found(self):
        response = self.app.get('/task/1')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Task not found"})

    def test_get_task(self):
        response = self.app.get('/task/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, "Task2")

    def test_post_task(self):
        response = self.app.post('/task/3', json={"description":"Task3"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"3":"Task3"})

    def test_post_task_already_exists(self):
        response = self.app.post('/task/4', json={"description":"Test4"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message":"Task already exists"})

    def test_post_task_wrong_key(self):
        response = self.app.post('/task/5', json={"desciption":"Task5"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message":"Missing 'description' key in request body"})  

    def test_put_task_not_found(self):
        response = self.app.put('/task/6', json={"description":"Task6"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message":"Task not found"})

    def test_put_task(self):
        response = self.app.put('/task/7', json={"description":"Test Task Update"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message":"Task updated successfully",
                                        "task_id": "7",
                                        "description": "Test Task Update"})
        
    def test_put_task_wrong_key(self):
        response = self.app.put('/task/8', json={"desciption":"Test Task Updated"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message":"Missing 'description' key in request body"})  
    
    def test_delete_task_not_found(self):
        response = self.app.delete('/task/9')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message":"Task not found"})

    def test_delete_task(self):
        response = self.app.delete('/task/10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message":"Task deleted succesfully"})

        
if __name__ == '__main__':
    unittest.main()