from src.convert_minutes_seconds import *

import unittest


class TestConvertMinutesSeconds(unittest.TestCase):
    def test_seconds_to_minutes(self):
        self.assertEqual(1000/60, convert_minutes_seconds(1000, "minutes"))

    def test_minutes_to_seconds(self):
        self.assertEqual(1000*60, convert_minutes_seconds(1000, "seconds"))

    def test_result_is_integer_or_float(self):
        self.assertTrue(isinstance(convert_minutes_seconds(1000, "minutes"), int) or
                        isinstance(convert_minutes_seconds(1000, "minutes"), float))


if __name__ == '__main__':
    unittest.main()
