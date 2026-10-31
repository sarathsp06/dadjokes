import unittest
from unittest.mock import MagicMock, patch
import requests

import main


class TestFetchJoke(unittest.TestCase):
	def test_fetch_joke_with_session_success(self):
		mock_session = MagicMock()
		mock_response = MagicMock()
		mock_response.json.return_value = {"joke": "Why did the chicken cross the road? To get to the other side."}
		mock_session.get.return_value = mock_response

		joke = main.fetch_joke(mock_session)

		self.assertEqual(joke, "Why did the chicken cross the road? To get to the other side.")
		mock_session.get.assert_called_once_with(
			'https://icanhazdadjoke.com/',
			headers={"Accept": "application/json"}
		)

	def test_fetch_joke_fallback_when_missing_key(self):
		mock_session = MagicMock()
		mock_response = MagicMock()
		mock_response.json.return_value = {}
		mock_session.get.return_value = mock_response

		joke = main.fetch_joke(mock_session)

		self.assertEqual(joke, "blah\n")

	@patch('requests.get')
	def test_fetch_joke_without_session(self, mock_get):
		mock_response = MagicMock()
		mock_response.json.return_value = {"joke": "I am a joke."}
		mock_get.return_value = mock_response

		joke = main.fetch_joke()

		self.assertEqual(joke, "I am a joke.")
		mock_get.assert_called_once_with(
			'https://icanhazdadjoke.com/',
			headers={"Accept": "application/json"}
		)


if __name__ == '__main__':
	unittest.main()
