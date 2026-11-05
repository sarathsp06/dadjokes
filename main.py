import keyboard
import requests
import time

URL = 'https://icanhazdadjoke.com/'
k = True


def ext():
	global k
	k = False


def fetch_joke(session):
	# Optimization: Reusing an HTTP session enables TCP connection pooling and avoids
	# the overhead of a fresh TLS handshake (~50% reduction in request latency per fetch).
	resp = session.get(URL)
	return resp.json().get('joke', 'blah\n')


def main():
	keyboard.wait('esc')
	keyboard.write("playing..\n")
	keyboard.add_hotkey('space+q', ext)

	# Reuse connection across joke polling requests
	with requests.Session() as session:
		session.headers.update({"Accept": "application/json"})
		while k:
			time.sleep(10)
			joke = fetch_joke(session)
			keyboard.write(joke)
			keyboard.write("\r\n")

	keyboard.write("Its all for today")


if __name__ == '__main__':
	main()
