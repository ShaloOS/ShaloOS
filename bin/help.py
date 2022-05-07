import configparser
from rich import print

config = configparser.ConfigParser()
config.read('bin/commands.ini')

for section in config.sections():
    option = 'name'
    print(f'{config[section][option]} - {config[section]["description"]}')