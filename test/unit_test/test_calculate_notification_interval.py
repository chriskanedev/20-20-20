from src.read_ini import read_ini
from src.calculate_notification_interval import *

import unittest


class TestCalculateNotificationInterval(unittest.TestCase):
    def test_calculation_works(self):
        config = read_ini("../../config.ini")
        self.assertEqual(1193, calculate_notification_interval(config))

    def test_result_is_integer(self):
        config = read_ini("../../config.ini")
        self.assertTrue(isinstance(calculate_notification_interval(config), int))

