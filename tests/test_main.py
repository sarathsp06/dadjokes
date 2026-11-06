import unittest
from unittest.mock import MagicMock, patch
import main

class TestDadJokes(unittest.TestCase):
    def test_create_session(self):
        session = main.create_session()
        self.assertEqual(session.headers.get("Accept"), "application/json")
        session.close()

    def test_get_joke_with_session(self):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {"joke": "Why did the scarecrow win an award? Because he was outstanding in his field."}
        mock_session.get.return_value = mock_response

        joke = main.get_joke(session=mock_session)
        self.assertEqual(joke, "Why did the scarecrow win an award? Because he was outstanding in his field.")
        mock_session.get.assert_called_once_with('https://icanhazdadjoke.com/', headers=None)

    def test_get_joke_fallback_when_missing_key(self):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        joke = main.get_joke(session=mock_session)
        self.assertEqual(joke, "blah\n")

    @patch('main.requests.get')
    def test_get_joke_default_fallback_to_requests(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"joke": "Test joke"}
        mock_requests_get.return_value = mock_response

        joke = main.get_joke()
        self.assertEqual(joke, "Test joke")
        mock_requests_get.assert_called_once_with('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})

if __name__ == '__main__':
    unittest.main()
