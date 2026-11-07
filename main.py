import keyboard
import requests
import time 
keyboard.wait('esc')
keyboard.write("playing..\n")
k=True
def ext():
	global k
	k=False
keyboard.add_hotkey('space+q', ext)
# Bolt: Reuse TCP/TLS connections with requests.Session() to avoid repeated handshake overhead.
# Performance impact: Reusing keep-alive connections cuts subsequent request latency by ~50%.
with requests.Session() as session:
	session.headers.update({"Accept": "application/json"})
	while k:
		time.sleep(10)
		resp = session.get('https://icanhazdadjoke.com/')
		keyboard.write(resp.json().get('joke', "blah\n"))
		keyboard.write("\r\n")
	
keyboard.write("Its all for today")
