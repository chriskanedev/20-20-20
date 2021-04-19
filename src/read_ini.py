from src.definitions import CONFIG_NAME

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


def get_first_char_from_configs(path):
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


def print_config(path):
    configurations = read_ini(path)

    for configuration in configurations:
        print(configuration, configurations[configuration])

