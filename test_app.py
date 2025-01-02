import unittest

from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self): # Create a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True 

    def test_get_task_not_found(self):
        response = self.app.get('/task/10')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Task not found"})

    def test_post_task(self):
        response = self.app.post('/task/10', json={"description":"Test Task"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"10":"Test Task"})

    def test_put_task_not_found(self):
        response = self.app.put('/task/1', json={"description":"Test Task"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message":"Task not found"})
         
if __name__ == '__main__':
    unittest.main()