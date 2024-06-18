import unittest
from app import create_app
import requests

class CompetitionTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        
    def test_get_find_by_id(self):
        response = requests.get('http://localhost:5000/api/v1/competition/1')
        self.assertEqual(response.status_code, 200)