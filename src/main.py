# Chris Kane | April 2021

from send_reminders import send_reminders
from read_ini import read_ini

config = read_ini("../config.ini")

send_reminders(config)
