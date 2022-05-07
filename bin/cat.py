import sys
import os
from rich import print

with open('tmp/cdir','r') as f: cdir = f.read()

try:
    if os.path.isfile(f'{cdir}/{sys.argv[1]}'):
        with open(f'{cdir}/{sys.argv[1]}', 'r') as f:
            print(f.read())
    elif os.path.isdir(f'{cdir}/{sys.argv[1]}'):
        print('You cant read a directory')
    elif not os.path.exists(f'{cdir}/{sys.argv[1]}'):
        print('File not found!')
except:
    print('You need to specify a file.')