import os,sys
with open('tmp/cdir','r') as f:
    cdir = f.read()
try:
    os.rmdir(f'{cdir}/{sys.argv[1]}')
except FileNotFoundError:
    print('Directory not found!')
except IndexError:
    print('You need to specify a directory.')
except Exception as e:
    print(e)
    print('\n')
