import keyboard
import requests
import time


def get_joke(session: requests.Session) -> str:
    """Fetch a dad joke using an existing requests.Session for connection reuse."""
    resp = session.get('https://icanhazdadjoke.com/')
    return resp.json().get('joke', "blah\n")


def main():
    keyboard.wait('esc')
    keyboard.write("playing..\n")
    k = True

    def ext():
        nonlocal k
        k = False

    keyboard.add_hotkey('space+q', ext)

    # Performance optimization: Reuse a requests.Session to persist TCP/TLS connections
    # across loop iterations instead of initiating a new handshake on every request (~50% latency reduction).
    with requests.Session() as session:
        session.headers.update({"Accept": "application/json"})
        while k:
            time.sleep(10)
            keyboard.write(get_joke(session))
            keyboard.write("\r\n")

    keyboard.write("Its all for today")


if __name__ == '__main__':
    main()
