import os,sys
from re import I
with open('tmp/cdir','r') as f:
    cdir = f.read()

if len(sys.argv) == 1:
    print(cdir)
elif '..' in sys.argv[1]:
    cdir = os.path.abspath(f'{cdir}/..')
elif sys.argv[1] == '.':
    pass
else:
    cdir = os.path.join(cdir,sys.argv[1])


if os.path.exists(f'{cdir}'):
    with open('tmp/cdir','w') as f:
        f.write(f'{cdir}')
else:
    print('Directory not found!')