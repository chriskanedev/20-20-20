import configparser
from DEFINITIONS import CONFIG_NAME

# Reads a config file dynamically to a dictionary which is returned


def read_ini(path):
    config = configparser.ConfigParser()
    config.read(path)

    configuration_file = config[CONFIG_NAME]
    configurations = dict()

    # Map to dictionary
    for configuration in configuration_file:
        configurations[configuration] = configuration_file[configuration]

    return configurations

