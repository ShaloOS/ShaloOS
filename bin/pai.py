# Python App Installer
import configparser,os,sys
from urllib.request import urlretrieve

config = configparser.ConfigParser()
config.read('bin/commands.ini')

def install(app_name):
    if config.has_section(app_name):
        print('App already exists')
        return
    else:
        url = f'https://raw.githubusercontent.com/ShaloOS/ShaloPackages/main/{app_name}.py'
        dst = f'bin/{app_name}.py'
        urlretrieve(url, dst)
        config.add_section(app_name)
        config.set(app_name, 'name', app_name)
        config.set(app_name, 'path', 'bin/' + app_name + '.py')
        with open('bin/commands.ini', 'w') as configfile:
            config.write(configfile)
        print('App created')

def remove_app(app_name):
    if config.has_section(app_name):
        config.remove_section(app_name)
        with open('bin/commands.ini', 'w') as configfile:
            config.write(configfile)
        os.remove(f'bin/{app_name}.py')
        print('App removed')
    else:
        print('App does not exist')

if len(sys.argv) >= 2:
    if sys.argv[1] == 'install' or sys.argv[1] == 'i':
        install(sys.argv[2])
    elif sys.argv[1] == 'remove' or sys.argv[1] == 'r':
        remove_app(sys.argv[2])
    else:
        print('Invalid command')
else:
    print('Invalid command')
    print('Usage: pai install <app_name>')
    print('Usage: pai remove <app_name>')