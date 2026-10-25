import keyboard
import requests
import time 

keyboard.wait('esc')
keyboard.write("playing..\n")
k = True

def ext():
	global k
	k = False

keyboard.add_hotkey('space+q', ext)

# Performance Optimization: Reuse TCP/TLS connections with requests.Session()
# to eliminate TLS handshake overhead on every GET request (~100-300ms savings per request).
session = requests.Session()

while k:
	time.sleep(10)
	resp = session.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
	keyboard.write(resp.json().get('joke', "blah\n"))
	keyboard.write("\r\n")

keyboard.write("Its all for today")
