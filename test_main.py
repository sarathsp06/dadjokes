import unittest
from unittest.mock import MagicMock
import requests
from main import get_joke


class TestGetJoke(unittest.TestCase):
    def test_get_joke_success(self):
        mock_session = MagicMock(spec=requests.Session)
        mock_response = MagicMock()
        mock_response.json.return_value = {"joke": "Why did the scarecrow win an award? Because he was outstanding in his field."}
        mock_session.get.return_value = mock_response

        joke = get_joke(mock_session)
        self.assertEqual(joke, "Why did the scarecrow win an award? Because he was outstanding in his field.")
        mock_session.get.assert_called_once_with('https://icanhazdadjoke.com/')

    def test_get_joke_fallback(self):
        mock_session = MagicMock(spec=requests.Session)
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        joke = get_joke(mock_session)
        self.assertEqual(joke, "blah\n")
        mock_session.get.assert_called_once_with('https://icanhazdadjoke.com/')


if __name__ == '__main__':
    unittest.main()
