from src.definitions import *

import unittest


class TestDefinitions(unittest.TestCase):
    def test_CONFIG_NAME_is_str(self):
        self.assertTrue(isinstance(CONFIG_NAME, str))

    def test_CONFIG_NAME_is_defined(self):
        self.assertTrue(len(CONFIG_NAME) > 1)

    def test_NOTIFICATION_ICON_PATH_is_str(self):
        self.assertTrue(isinstance(NOTIFICATION_ICON_PATH, str))

    def test_NOTIFICATION_ICON_PATH_is_defined(self):
        self.assertTrue(len(NOTIFICATION_ICON_PATH) > 1)

    def test_NOTIFICATION_ICON_PATH_is_ico_file_type(self):
        self.assertTrue(NOTIFICATION_ICON_PATH[-4:] == ".ico")


if __name__ == '__main__':
    unittest.main()
