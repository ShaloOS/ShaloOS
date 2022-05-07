import os
import sys
with open('tmp/cdir', 'r') as f:
    cdir = f.read()
if os.path.exists(f'{cdir}/{sys.argv[1]}'):
    prefix = 'python3'
    if os.name == 'nt': prefix = 'py'
    os.system(f'{prefix} {cdir}/{sys.argv[1]}')
else:
    print('File not found')