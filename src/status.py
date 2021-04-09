from DEFINITIONS import *

import time
import win32api
from notification import display_notification


def send_reminders():
    current_system_code = 0
    secs_since_last_active = 0
    secs_since_last_away = 0
    while REMINDERS_ENABLED is True:
        new_system_code = win32api.GetLastInputInfo()

        if current_system_code == new_system_code:
            active = False
        else:
            active = True

        if active is False:
            secs_since_last_active += 1
        else:
            secs_since_last_active = 0

        if secs_since_last_active >= SECS_TILL_STATUS_IS_AWAY:
            away = True
        else:
            away = False

        if away is False:
            secs_since_last_away += 1
        else:
            secs_since_last_away = 0

        if secs_since_last_away >= REMINDER_INTERVAL:
            display_notification()
            secs_since_last_away = 0

        current_system_code = new_system_code
        time.sleep(1)


send_reminders()
