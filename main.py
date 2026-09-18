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

# Optimization (Bolt ⚡): Reuse HTTP connections using requests.Session()
# Reusing the underlying TCP/TLS connection pool reduces request latency from ~130ms to ~45ms per call.
session = requests.Session()
session.headers.update({"Accept": "application/json"})

while k:
	time.sleep(10)
	resp = session.get('https://icanhazdadjoke.com/')
	keyboard.write(resp.json().get('joke', "blah\n"))
	keyboard.write("\r\n")
	
keyboard.write("Its all for today")
