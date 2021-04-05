from win10toast import ToastNotifier
import time
import win32api
from threading import Thread

toaster = ToastNotifier()
#toaster.show_toast("20-20-20 Reminder", "It's time to take a short break from your screen. Every 20 minutes, look at an object 20 meters away for 20 seconds.", icon_path="favicon.ico", duration=60)

def firstFunction():
    while True:
        print("HI")
        time.sleep(1.5)


def secondFunction():
    while True:
        print(win32api.GetLastInputInfo())
        time.sleep(1)


t1 = Thread(target=firstFunction)
t2 = Thread(target=secondFunction)

t1.start()
t2.start()