from src.read_ini_class import ReadINI

import unittest
from unittest.mock import MagicMock


class Mock(unittest.TestCase):
    path = "../config.ini"

    def test_get_first_char_from_configs(self):
        propertyData = ['y', '2', '1', '2', 'I', '7']
        configProvider = ReadINI()
        configProvider.get_first_char_from_configs = MagicMock(return_value=propertyData)
        result = configProvider.get_first_char_from_configs(self.path)
        self.assertEqual(['y', '2', '1', '2', 'I', '7'], result)


if __name__ == '__main__':
    unittest.main()
