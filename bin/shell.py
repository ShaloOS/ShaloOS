import configparser
import platform
import os
from rich import print
from rich.console import Console
from rich.prompt import Prompt
console = Console()

config = configparser.ConfigParser()
config.read('bin/commands.ini')

def as_dict():
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)
    return dictionary

d = as_dict()

def getProp(property,app):
    prop = d.get(app)
    prop2 = prop.get(property)
    return prop2
def Exists(app):
    if config.has_section(app.lower()):
        return True
    else:
        return False
def openapp(app, args):
    if app.lower() == "exit":
        try:
            code = int(args[0])
        except:
            code = 0
        exit(code)
    if Exists(app):
        python = "python" if platform.system() == "Windows" else "python3"
        global inp_onlyargs
        inp_onlyargs = ' '.join(inp_onlyargs)
        os.system(f'{python} {getProp("path", app)} {inp_onlyargs}')
    elif app == "":
        pass
    else:
        print('Command or application not found!')

def reload():
    init_prompt()


def init_prompt():
    with open('.session','r') as f:
        user = f.read()
    with open('etc/hostname','r') as f:
        host = f.read()
    f = open(f'users/{user}/.dshellrc', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.splitlines()[0]
        if line.startswith('theme '):
            theme = line.split(' ')[1:]
            theme = ' '.join(theme)
            theme = theme.lower()
    global prompt
    if theme != "":
        prompt = f'[{theme}]{user}[/{theme}][bold {theme}]@[/bold {theme}][{theme}]{host}[/{theme}]'
    else:
        prompt = f'{user}@{host}'
init_prompt()
while True:
    config.read('bin/commands.ini')
    d = as_dict()
    init_prompt()
    inp = Prompt.ask(prompt)
    inp_transformed = inp.split(' ',1)
    inp_onlyargs = inp.split(' ')
    inp_onlyargs.pop(0)
    openapp(inp_transformed[0],inp_onlyargs)