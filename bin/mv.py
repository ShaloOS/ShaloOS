import os,sys
with open('tmp/cdir','r') as f:
    cdir = f.read()
try:
    os.rename(f'{cdir}/{sys.argv[1]}',f'{cdir}/{sys.argv[2]}')
except FileNotFoundError:
    print('File not found!')
except IndexError:
    print('You need to specify a file.')
except Exception as e:
    print(e)
    print('\n')
