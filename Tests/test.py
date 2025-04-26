"""
test.py

This is the main file for the Flask App that serves as 
a web interface for the data processing functions."""
import unittest
from app import app

class FlaskAppTest(unittest.TestCase):
    """Test cases for the Flask App."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        """Get / should return the welcome message 
        starting with 'Welcome to the Flask App!'."""
        response = self.client.get('/')
        self.assertTrue(response.data.startswith(
            b'<strong>Welcome to the Flask App!'))

    def test_data_overview(self):
        """Get /dataOverview should return something (the loaded data)."""
        response = self.client.get('/dataOverview')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_sell_arrests_valid(self):
        """Get /<int>/<int> should return the number of people arrested for selling drugs."""
        response = self.client.get('/1/10')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'566 people', response.data)

    def test_sell_arrests_invalid(self):
        """Get /<non-int>/<non-int> should return the invalid-input message."""
        response = self.client.get('/a/b')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Invalid input. Please provide valid integers for lower and upper bounds.',
            response.data
        )
    def test_sell_arrests_invalid_int(self):
        """Get /<int>/<non-int> should return the invalid-input message."""
        response = self.client.get('/1/b')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Invalid input. Please provide valid integers for lower and upper bounds.',
            response.data
        )

if __name__ == '__main__':
    unittest.main()
