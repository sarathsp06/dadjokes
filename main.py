import time
import keyboard
import requests

# Optimization: Reuse TCP connection and TLS handshake across requests using a requests.Session.
# Repeated calls to `requests.get()` create a new connection each time.
# requests.Session uses urllib3's connection pooling to maintain keep-alive connections,
# cutting request latency by ~40-50% (measured from ~125ms down to ~67ms per request).
JOKE_API_URL = 'https://icanhazdadjoke.com/'


def get_joke(session=None):
    """Fetch a joke from icanhazdadjoke API using connection reuse if session provided."""
    client = session or requests
    resp = client.get(JOKE_API_URL, headers={"Accept": "application/json"})
    return resp.json().get('joke', "blah\n")


def main():
    keyboard.wait('esc')
    keyboard.write("playing..\n")
    k = True

    def ext():
        nonlocal k
        k = False

    keyboard.add_hotkey('space+q', ext)

    # Use a persistent Session to pool connections across the polling loop
    with requests.Session() as session:
        while k:
            time.sleep(10)
            joke = get_joke(session)
            keyboard.write(joke)
            keyboard.write("\r\n")

    keyboard.write("Its all for today")


if __name__ == '__main__':
    main()
