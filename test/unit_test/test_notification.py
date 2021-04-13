from src.read_ini import read_ini
from src.notification import *

import unittest


class TestNotification(unittest.TestCase):
    def test_display_notifications(self):
        config = read_ini("../../config.ini")
        icon_path = "../../resource/favicon.ico"
        self.assertTrue(display_notification(config, icon_path))

