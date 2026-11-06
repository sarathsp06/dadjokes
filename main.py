import keyboard
import requests
import time

# Bolt Optimization: Reuse a requests.Session to enable HTTP connection pooling.
# Reusing the TCP/TLS connection across repeated calls eliminates the ~200-300ms
# handshake overhead per request to https://icanhazdadjoke.com/.
def create_session():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    return session

def get_joke(session=None):
    client = session or requests
    headers = {"Accept": "application/json"} if session is None else None
    resp = client.get('https://icanhazdadjoke.com/', headers=headers)
    return resp.json().get('joke', "blah\n")

k = True

def ext():
    global k
    k = False

def main():
    keyboard.wait('esc')
    keyboard.write("playing..\n")
    keyboard.add_hotkey('space+q', ext)

    # Use a persistent session to keep HTTP connection alive between intervals
    with create_session() as session:
        while k:
            time.sleep(10)
            joke = get_joke(session)
            keyboard.write(joke)
            keyboard.write("\r\n")

    keyboard.write("Its all for today")

if __name__ == '__main__':
    main()
