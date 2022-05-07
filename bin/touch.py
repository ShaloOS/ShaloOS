import os,sys
with open('tmp/cdir','r') as f:
    cdir = f.read()
try:
    with open(f'{cdir}/{sys.argv[1]}','w') as f:
        pass
except FileExistsError:
    print('File already exists!')
except IndexError:
    print('You need to specify a file.')
except Exception as e:
    print(e)
    print('\n')
    