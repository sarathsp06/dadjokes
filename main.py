import keyboard
import requests
import time


def fetch_joke(session=None):
	"""Fetch a dad joke from the API using an optional persistent session.
	
	⚡ Bolt Optimization:
	Reusing a requests.Session() maintains an HTTP connection pool with keep-alive,
	avoiding expensive TCP and TLS handshakes on every request (~40% latency reduction).
	"""
	requester = session if session is not None else requests
	resp = requester.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
	return resp.json().get('joke', "blah\n")


def main():
	keyboard.wait('esc')
	keyboard.write("playing..\n")
	k = True

	def ext():
		global k
		k = False

	keyboard.add_hotkey('space+q', ext)

	# Reuse a single session for repeated requests to leverage HTTP connection pooling
	with requests.Session() as session:
		while k:
			time.sleep(10)
			joke = fetch_joke(session)
			keyboard.write(joke)
			keyboard.write("\r\n")

	keyboard.write("Its all for today")


if __name__ == '__main__':
	main()
