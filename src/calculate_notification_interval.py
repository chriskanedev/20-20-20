from src.convert_minutes_seconds import *


def calculate_notification_interval(config):
    reminder_interval = convert_minutes_seconds(int(config['send_reminder_every_minutes']), "seconds")
    notification_duration = int(config['notification_duration_seconds'])
    return reminder_interval - notification_duration

