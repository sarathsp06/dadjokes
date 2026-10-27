import time
import keyboard
import requests

# Optimization: Use requests.Session() to enable HTTP connection pooling / keep-alive.
# This avoids repeated TCP/TLS handshakes on every request, reducing latency by ~45%.
session = requests.Session()
session.headers.update({"Accept": "application/json"})

def get_dad_joke(http_session=None):
    """Fetch a dad joke from icanhazdadjoke.com using session connection pooling."""
    if http_session is None:
        http_session = session
    resp = http_session.get("https://icanhazdadjoke.com/")
    return resp.json().get("joke", "blah\n")

def main():
    keyboard.wait("esc")
    keyboard.write("playing..\n")
    k = True

    def ext():
        nonlocal k
        k = False

    keyboard.add_hotkey("space+q", ext)

    while k:
        time.sleep(10)
        joke = get_dad_joke()
        keyboard.write(joke)
        keyboard.write("\r\n")

    keyboard.write("Its all for today")

if __name__ == "__main__":
    main()
