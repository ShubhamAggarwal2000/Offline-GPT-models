import unittest
from app import app  # Import the Flask app instance


class TestApp(unittest.TestCase):

    def test_chat_route(self):
        """
        Test the /chat route
        """
        with app.test_client() as client:
            response = client.post('/chat', json={'message': 'Hi there!'})
            self.assertEqual(response.status_code, 200)
            # Check if the response contains a 'response' key
            self.assertIn('response', response.json)

    def test_train_route(self):
        """
        Test the /train route
        """
        with app.test_client() as client:

            # Send sample training data
            response = client.post(
                '/train', json={'data': 'New training data'})

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'status': 'success'})


if __name__ == '__main__':
    unittest.main()  # Run test cases
