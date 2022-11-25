#!/bin/python3

import time
from datetime import datetime
import threading as th
import subprocess as s
import os

clear = lambda: os.system('clear')

pomodoro = 60 * 40
pause = 60 * 5

keep_going = True
def kc_thread():
    global keep_going
    input()
    keep_going = False

def timer(t):
    th.Thread(target=kc_thread, args=(), name='kc_thread', daemon=True).start()
    start = time.time()
    while keep_going:
        now = time.time()
        count = int(start - now + t)
        mins, secs = divmod(abs(count), 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")

        time.sleep(1)
        if count == 0:
            notify()

def start_pom(length):
    start = time.time()
    timer(length)
    end = time.time()
    diff = end-start
    return diff

def notify():
    #s.call(['notify-send','Pomodoro-Timer','Time is up!'])
    os.system("notify-send 'Pomodoro-Timer' 'Time is up!' --icon=$PWD'/tomato.png' --expire-time 60000")

while True:
	clear()
	print("Pomodoro:")
	keep_going = True
	x = start_pom(pomodoro)
	y = [str(datetime.today()), "   " +str(x) + "\n"]
	print(y)
	File_object = open(r"pomodoro_history.txt", "a")
	File_object.writelines(y)
	File_object.close()

	clear()
	print("Pause:")
	keep_going = True
	start_pom(pause)
	



