from DEFINITIONS import *

import time
import win32api
from notification import display_notification


def calculate_status():
    current_system_code = 0
    time_elapsed = 0
    secs_since_last_active = 0
    while True:
        new_system_code = win32api.GetLastInputInfo()
        if current_system_code == new_system_code:
            active = False
        else:
            active = True
            time_elapsed = 0

        if active is False:
            secs_since_last_active += 1
        else:
            secs_since_last_active = 0

        if secs_since_last_active >= SECS_TILL_STATUS_IS_AWAY:
            away = True
        else:
            away = False

        if time_elapsed >= 1200 and away is False:
            display_notification()
            time_elapsed = 0

        print(time_elapsed, away, secs_since_last_active)

        current_system_code = new_system_code
        time.sleep(1)
        time_elapsed += 1


calculate_status()
