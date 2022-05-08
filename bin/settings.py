from rich import print
from rich.prompt import Prompt
colors = ['magenta', 'cyan', 'yellow', 'green', 'blue', 'red', 'white', 'black']

def color_chooser():
    global modified_whole_file
    for color in colors:
        num = colors.index(color) + 1
        print(f'[{num}] - {color}')
    print('\n')
    option_c = Prompt.ask('Choose a color: ')
    fcolor = colors[int(option_c) - 1]
    with open('.session', 'r') as f:
        user = f.read()
    with open(f'users/{user}/.dshellrc','r') as f:
        whole_file = f.read()
        for line in whole_file.split('\n'):
            if 'theme ' in line:
                line_new = f'theme {fcolor}'
                modified_whole_file = whole_file.replace(line, line_new)
    with open(f'users/{user}/.dshellrc','w') as f:
        f.write(modified_whole_file)

    print(whole_file)
    print(f'Color changed to {fcolor}')
print('Here you can modify your settings.')
print('[1] - Change color')

option = Prompt.ask('Choose an option: ')
if option == '1':
    color_chooser()
else:
    print('Invalid option.')
