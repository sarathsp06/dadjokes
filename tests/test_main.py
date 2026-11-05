import unittest
from unittest.mock import MagicMock
import main


class TestMain(unittest.TestCase):
    def test_fetch_joke_success(self):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {'id': '123', 'joke': 'Why did the chicken cross the road?', 'status': 200}
        mock_session.get.return_value = mock_response

        joke = main.fetch_joke(mock_session)
        self.assertEqual(joke, 'Why did the chicken cross the road?')
        mock_session.get.assert_called_once_with(main.URL)

    def test_fetch_joke_fallback(self):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        joke = main.fetch_joke(mock_session)
        self.assertEqual(joke, 'blah\n')
        mock_session.get.assert_called_once_with(main.URL)

    def test_ext(self):
        main.k = True
        main.ext()
        self.assertFalse(main.k)


if __name__ == '__main__':
    unittest.main()
