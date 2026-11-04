import unittest
from unittest.mock import MagicMock
import main

class TestJokeFetching(unittest.TestCase):
    def test_create_session_headers(self):
        session = main.create_session()
        self.assertEqual(session.headers.get("Accept"), "application/json")
        session.close()

    def test_fetch_joke_success(self):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {"joke": "Why did the chicken cross the road? To get to the other side."}
        mock_session.get.return_value = mock_response

        joke = main.fetch_joke(mock_session)
        mock_session.get.assert_called_once_with(main.API_URL)
        self.assertEqual(joke, "Why did the chicken cross the road? To get to the other side.")

    def test_fetch_joke_fallback(self):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        joke = main.fetch_joke(mock_session)
        mock_session.get.assert_called_once_with(main.API_URL)
        self.assertEqual(joke, "blah\n")

if __name__ == "__main__":
    unittest.main()
