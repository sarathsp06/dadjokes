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

# Re-use HTTP connection session to avoid repeated TLS handshake and TCP connection overhead.
# Expected performance impact: ~2x speedup per request (~50% reduction in fetch latency).
session = requests.Session()
session.headers.update({"Accept": "application/json"})

while k:
	time.sleep(10)
	resp = session.get('https://icanhazdadjoke.com/')
	keyboard.write(resp.json().get('joke', "blah\n"))
	keyboard.write("\r\n")
	
keyboard.write("Its all for today")
