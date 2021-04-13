from win10toast import ToastNotifier


def display_notification(config, icon_path):
    toaster = ToastNotifier()
    toaster.show_toast(config['notification_title'], config['notification_description'],
                       icon_path=icon_path, duration=int(config['notification_duration_seconds']))
    return True

