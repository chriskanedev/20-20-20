from src.definitions import CONFIG_NAME

import configparser


class ReadINI:
    def get_first_char_from_configs(self, path):
        config = configparser.ConfigParser()
        config.read(path)

        configuration_file = config[CONFIG_NAME]
        configurations = dict()
        chars = list()

        # Map to dictionary
        for configuration in configuration_file:
            configurations[configuration] = configuration_file[configuration]
            chars.append(configurations[configuration][0])

        return chars

