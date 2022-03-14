from re import T
from turtle import exitonclick
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
while k:
	time.sleep(10)
	resp=requests.get('https://icanhazdadjoke.com/',headers={ "Accept":"application/json"})
	keyboard.write(resp.json().get('joke',"blah\n"))
	keyboard.write("\r\n")
	
keyboard.write("Its all for today")