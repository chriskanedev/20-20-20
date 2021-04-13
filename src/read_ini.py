from DEFINITIONS import CONFIG_NAME

import configparser


def read_ini(path):
    config = configparser.ConfigParser()
    config.read(path)

    configuration_file = config[CONFIG_NAME]
    configurations = dict()

    # Map to dictionary
    for configuration in configuration_file:
        configurations[configuration] = configuration_file[configuration]

    return configurations

