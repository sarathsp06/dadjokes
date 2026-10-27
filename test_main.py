import unittest
from unittest.mock import MagicMock
from main import get_dad_joke, session

class TestDadJokes(unittest.TestCase):
    def test_get_dad_joke_success(self):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {"joke": "Why don't eggs tell jokes? They'd crack up."}
        mock_session.get.return_value = mock_response

        joke = get_dad_joke(http_session=mock_session)
        self.assertEqual(joke, "Why don't eggs tell jokes? They'd crack up.")
        mock_session.get.assert_called_once_with("https://icanhazdadjoke.com/")

    def test_get_dad_joke_fallback(self):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        joke = get_dad_joke(http_session=mock_session)
        self.assertEqual(joke, "blah\n")

    def test_session_headers(self):
        self.assertEqual(session.headers.get("Accept"), "application/json")

if __name__ == "__main__":
    unittest.main()
