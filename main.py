import sys
import time
import requests

API_URL = "https://icanhazdadjoke.com/"

def create_session() -> requests.Session:
    """Create and configure a requests.Session.

    Reusing a Session object keeps the underlying TCP/TLS connection open
    (HTTP Keep-Alive), saving connection handshake latency (~100-200ms)
    on every subsequent request.
    """
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    return session

def fetch_joke(session: requests.Session) -> str:
    """Fetch a random dad joke using a persistent session."""
    resp = session.get(API_URL)
    return resp.json().get("joke", "blah\n")

def run():
    import keyboard

    keyboard.wait("esc")
    keyboard.write("playing..\n")
    k = True

    def ext():
        nonlocal k
        k = False

    keyboard.add_hotkey("space+q", ext)

    # Bolt optimization: reuse Session across loop iterations to avoid repeated TCP+TLS handshakes
    with create_session() as session:
        while k:
            time.sleep(10)
            joke = fetch_joke(session)
            keyboard.write(joke)
            keyboard.write("\r\n")

    keyboard.write("Its all for today")

if __name__ == "__main__":
    run()
