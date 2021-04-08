from DEFINITIONS import *

from win10toast import ToastNotifier


def display_notification():
    toaster = ToastNotifier()
    toaster.show_toast(NOTIFICATION_TITLE, NOTIFICATION_DESCRIPTION, icon_path=NOTIFICATION_ICON_PATH,
                       duration=NOTIFICATION_DURATION)
