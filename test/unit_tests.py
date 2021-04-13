import unittest
from src.calculate_notification_interval import *
from src.notification import *


class TestNotification(unittest.TestCase):
    def test_display_notifications(self):
        self.assertTrue(display_notification())


class TestCalculateInterval(unittest.TestCase):
    def test_calculation_works(self):
        self.assertEqual(5, calculate_notification_interval(10, 5))

    def test_result_is_integer(self):
        self.assertTrue(isinstance(calculate_notification_interval(REMINDER_INTERVAL, NOTIFICATION_DURATION), int))


if __name__ == '__main__':
    unittest.main()
