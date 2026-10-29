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

# Re-use TCP connection using requests.Session() to enable HTTP Keep-Alive
# and avoid repeated TLS handshakes for each joke fetch (~100-300ms saved per request).
session = requests.Session()
session.headers.update({"Accept": "application/json"})

while k:
	time.sleep(10)
	resp = session.get('https://icanhazdadjoke.com/')
	keyboard.write(resp.json().get('joke', "blah\n"))
	keyboard.write("\r\n")
	
keyboard.write("Its all for today")
