import os,sys
prefix = "python3"
if os.name == "nt":
    prefix = "py"

if '--dev' in sys.argv:
    with open('.session','w') as f:
        f.write('Geri')
    os.system(f'{prefix} bin/shell.py')

os.system(f'{prefix} bin/login.py')