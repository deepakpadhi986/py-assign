import unittest
import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_generate_response(self):
        prompt = "Q: What is the meaning of life?\nA:"
        response = app.generate_response(prompt)
        self.assertIsInstance(response, str)

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ask a question or enter a prompt:', response.data)

    def test_submit_message(self):
        response = self.app.post('/result', data=dict(prompt='What is the meaning of life?'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You Asked:', response.data)

if __name__ == '__main__':
    unittest.main()

