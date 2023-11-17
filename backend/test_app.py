import unittest
from app import app  # Import the Flask app instance


class TestApp(unittest.TestCase):

    def test_chat_route(self):
        """
        Test the /chat route
        """
        # Context manager allows accessing test client
        with app.test_client() as client:

            # Send a sample chat message
            response = client.post('/chat', json={'message': 'Hi there!'})

            # Assert response status code
            self.assertEqual(response.status_code, 200)

            # Assert response data
            self.assertEqual(response.json, {'response': 'Hello!'})

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
