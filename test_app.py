import unittest
from app import app

class BasicTests(unittest.TestCase):
	
	def setUp(self):
		# set up a test client
		self.app = app.test_client()
		self.app.testing = True
	
	def test_main_page(self):
	    #Send Get on '/'
	    response = self.app.get('/')
	    self.assertEqual(response.status_code, 200)
	    self.assertEqual(response.data, b'Hello, World!')
	
if __name__ == "__main__":
    unittest.main()
