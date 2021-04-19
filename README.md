# 20-20-20
It has been suggested that the 20, 20, 20 rule could be beneficial in reducing the chance of eye-strain caused by computer usage.

[The Royal National Institute of Blind People advice](https://www.rnib.org.uk/eye-health/looking-after-your-eyes/safe-eyes) is:
"The 20, 20, 20 rule suggests taking a break of at least 20 seconds, every 20 minutes and to look at least 20 feet away."

This is an open source and fully customisable app for Windows 10 which will send a reminder to the user every 20 minutes to help them follow the 20, 20, 20 rule.

## Installation and Usage
A end-user friendly installation process is coming soon.

Clone or download the repository and run [src/main.py](https://github.com/chriskanedev/20-20-20/blob/master/src/main.py) in a Python IDE. The reccomended IDE is [JetBrains PyCharm](https://www.jetbrains.com/pycharm/download/). 20-20-20 Reminders will automatically be sent based upon the User Configuration.

## User Configuration
### [config.ini](https://github.com/chriskanedev/20-20-20/blob/master/config.ini)
- enable_reminders | Reminders will only be sent when this is set to y. The default is: y.
- send_reminder_every_minutes | This is the duration between reminders. The default is: 20.
- status_away_after_minutes | The user is considered away from the computer after this many minutes. The default is: 10.
- notification_title | This is the name of the Windows 10 'Toast' notification. The default is: 20-20-20 Reminder.
- notification_description | This is the reminder message. The default is: It's time to take a break from your screen. Every 20 minutes, look at something at least 20 feet away for 20 seconds.
- notification_duration_seconds | This is how long the notification will persist in the Notification Area. Notications persist on the screen for 5 seconds but it takes a couple of more seconds to clear the notification from the screen with a swipe transition. It is recommended to keep this configuration at a minimum of 7 but this can be increased to keep the reminder in the Notification Area for longer. You can't control how long the notification actually stays on the screen. The default is: 20.

## Testing
### Unit Testing
This app has a comprehensive [Unit Test](https://github.com/chriskanedev/20-20-20/tree/master/test/unit_test) suite. A seperate unit test file is used to test 4 of 7 source files.

To run all unit tests at once, run [all_unit_test.py](https://github.com/chriskanedev/20-20-20/blob/master/test/unit_test/all_unit_test.py).

### Data Load Doubling Functions

[Read INI file configuration](https://github.com/chriskanedev/20-20-20/blob/master/src/read_ini.py).

### Mocking
The class for the mock is [ReadINI](https://github.com/chriskanedev/20-20-20/blob/master/src/read_ini_class.py).

[Link to the mock](https://github.com/chriskanedev/20-20-20/blob/master/test/mock.py).
