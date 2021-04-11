from DEFINITIONS import *
from notification import *
from calculate_interval import *

import time
import win32api


def send_reminders():
    current_system_code = 0
    secs_since_last_active = 0
    secs_since_last_away = 0
    defined_interval = calculate_notification_interval(REMINDER_INTERVAL, NOTIFICATION_DURATION)

    while REMINDERS_ENABLED is True:
        new_system_code = win32api.GetLastInputInfo()

        # Check if user is currently active
        if current_system_code == new_system_code:
            active = False
        else:
            active = True

        # Calculate seconds since last active
        if active is False:
            secs_since_last_active += 1
        else:
            secs_since_last_active = 0

        # Check if user is currently away
        if secs_since_last_active >= SECS_TILL_STATUS_IS_AWAY:
            away = True
        else:
            away = False

        # Calculate seconds since last away
        if away is False:
            secs_since_last_away += 1
        else:
            secs_since_last_away = 0

        # Send notification if user has not been away for more than the defined interval (20 minutes as default)
        if secs_since_last_away >= defined_interval:
            display_notification()
            secs_since_last_away = 0

        current_system_code = new_system_code
        time.sleep(1)


send_reminders()
