import os,sys
with open('tmp/cdir','r') as f:
    cdir = f.read()
try:
    os.mkdir(f'{cdir}/{sys.argv[1]}')
except FileExistsError:
    print('Directory already exists!')
except IndexError:
    print('You need to specify a directory name.')
except Exception as e:
    print(e)
    print('\n')