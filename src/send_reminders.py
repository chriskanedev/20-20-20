from notification import *
from calculate_notification_interval import *

import time
import win32api


def send_reminders(config):
    current_system_code = 0
    secs_since_last_active = 0
    secs_since_last_away = 0
    defined_interval = calculate_notification_interval(config)

    while config['enable_reminders'] == "y":
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
        status_away_after_seconds = convert_minutes_seconds(config['status_away_after_minutes'], "seconds")
        if secs_since_last_active >= status_away_after_seconds:
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
            display_notification(config)
            secs_since_last_away = 0

        current_system_code = new_system_code
        time.sleep(1)

