from DEFINITIONS import NOTIFICATION_ICON_PATH

from win10toast import ToastNotifier


def display_notification(config):
    toaster = ToastNotifier()
    toaster.show_toast(config['notification_title'], config['notification_description'],
                       icon_path=NOTIFICATION_ICON_PATH, duration=int(config['notification_duration_seconds']))
    return True

