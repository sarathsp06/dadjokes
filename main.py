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
# Use a persistent requests.Session to reuse underlying TCP/TLS connections
# across repeated HTTP requests, avoiding repeated handshake latencies.
session = requests.Session()
session.headers.update({"Accept": "application/json"})

while k:
	time.sleep(10)
	resp = session.get('https://icanhazdadjoke.com/')
	keyboard.write(resp.json().get('joke',"blah\n"))
	keyboard.write("\r\n")
	
keyboard.write("Its all for today")
