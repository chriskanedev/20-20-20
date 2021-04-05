
import time
import win32api
from threading import Thread



def firstFunction():
    while True:
        print("HI")
        time.sleep(2)


def secondFunction():
    new_system_code = 0
    current_system_code = 0
    time_elapsed = 0
    active = False
    while True:
        if current_system_code == current_system_code

        current_system_code = win32api.GetLastInputInfo()
        time.sleep(1)
        time_elapsed += 1

        print(time_elapsed, current_system_code)


t1 = Thread(target=firstFunction)
t2 = Thread(target=secondFunction)

t1.start()
t2.start()