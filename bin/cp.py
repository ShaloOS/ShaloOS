import shutil,sys
with open('tmp/cdir','r') as f:
    cdir = f.read()
try:
    shutil.copy(f'{cdir}/{sys.argv[1]}',f'{cdir}/{sys.argv[2]}')
except FileNotFoundError:
    print('File not found!')
except IndexError:
    print('You need to specify a file.')
except shutil.SameFileError:
    print('Source and destination are the same!')
except Exception as e:
    print(e)
    print('\n')
