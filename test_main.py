import unittest
from unittest.mock import MagicMock, patch
import requests
import main
from main import get_joke, JOKE_API_URL


class TestGetJoke(unittest.TestCase):
    def test_get_joke_with_session(self):
        mock_session = MagicMock(spec=requests.Session)
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "123", "joke": "Why did the chicken cross the road?", "status": 200}
        mock_session.get.return_value = mock_response

        joke = get_joke(session=mock_session)

        mock_session.get.assert_called_once_with(JOKE_API_URL, headers={"Accept": "application/json"})
        self.assertEqual(joke, "Why did the chicken cross the road?")

    def test_get_joke_fallback(self):
        mock_session = MagicMock(spec=requests.Session)
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_session.get.return_value = mock_response

        joke = get_joke(session=mock_session)

        self.assertEqual(joke, "blah\n")

    @patch('main.time.sleep')
    @patch('main.keyboard')
    @patch('main.get_joke')
    def test_main_loop_exit_hotkey(self, mock_get_joke, mock_keyboard, mock_sleep):
        # Verify that triggering the ext hotkey stops the main loop cleanly
        mock_get_joke.return_value = "Test joke"

        def simulate_hotkey(hotkey, callback):
            if hotkey == 'space+q':
                # Call callback after 1 iteration in mock_sleep
                def side_effect(seconds):
                    callback()
                mock_sleep.side_effect = side_effect

        mock_keyboard.add_hotkey.side_effect = simulate_hotkey

        main.main()

        mock_keyboard.wait.assert_called_once_with('esc')
        mock_keyboard.write.assert_any_call("playing..\n")
        mock_keyboard.write.assert_any_call("Test joke")
        mock_keyboard.write.assert_any_call("\r\n")
        mock_keyboard.write.assert_any_call("Its all for today")
        self.assertEqual(mock_get_joke.call_count, 1)


if __name__ == '__main__':
    unittest.main()
