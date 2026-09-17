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
# Use a requests.Session() instance for HTTP Keep-Alive / connection pooling.
# Reusing TCP connections avoids redundant DNS lookups, TCP handshakes, and TLS negotiation
# on every joke request, reducing network latency and CPU load per request.
session = requests.Session()

while k:
	time.sleep(10)
	resp=session.get('https://icanhazdadjoke.com/',headers={ "Accept":"application/json"})
	keyboard.write(resp.json().get('joke',"blah\n"))
	keyboard.write("\r\n")
	
keyboard.write("Its all for today")
