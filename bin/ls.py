from genericpath import isdir
import os,sys
from rich import print

with open('tmp/cdir','r') as f:
    cdir = f.read()
try:
    if sys.argv[1].lower() == '--hidden':
        ssf = False
    else:
        ssf = True
except:
    ssf = True
for i in os.listdir(cdir):
    if i.endswith('.py'):
        print(':snake: -', i)
    elif ssf and i.startswith('.'):
        pass
    elif i.endswith('.js'):
        print(':book: -', i)
    elif isdir(f'{cdir}/{i}'):
        if i == 'Desktop':
            print(':computer: -', i)
        elif i == 'tmp':
            print(':clock1: -', i)
        elif i == 'etc':
            print(':file_cabinet: -', i)
        elif i == 'users':
            print(':busts_in_silhouette: -', i)
        elif i == 'bin':
            print(':gear: -', i)
        else:
            print(':file_folder: -', i)
    else:
        print(i)
print('\n')