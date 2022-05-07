import os,hashlib
from rich import print
from rich.prompt import Prompt

if os.path.exists('users/'):
    try:
        os.remove('.session')
    except:
        pass
    print("Welcome back to shalo os! \n Please log in to proceed.")
    print("Avalible users:")
    for user in os.listdir('users/'):
        print(user)
    print("\n")
    user = Prompt.ask("Username")
    if user in os.listdir('users/'):
        password = Prompt.ask("Password",password=True)
        with open(f'users/{user}/.passfile', 'r') as f:
            if hashlib.sha256(password.encode()).hexdigest() == f.read():
                print("Logged in!")
                with open('.session','w') as f:
                    f.write(user)
                os.system(f'python3 bin/shell.py {user}')
            else:
                print("Wrong password!")
                os.system(f'python3 bin/login.py')
else:
    print("Welcome to shalo os! \n This guide will help you configure the os to your liking.")
    print("\n")
    print("Please wait until we install the necessary dependencies...")
    prefix = 'python3'
    if os.name == 'nt': prefix = 'py'
    os.system(f'{prefix} -m pip install rich --user')
    print("First, we need to create a user.")
    print("\n")
    user = Prompt.ask("Username")
    print('\n')
    print(f'Welcome {user}! Now we need to make you a password.')
    passw = Prompt.ask("Password",password=True)
    print('\n')
    print("Please hold on while we create your account.")
    try:
        os.mkdir('users/')
    except FileExistsError:
        pass
    try:
        os.mkdir(f'users/{user}')
    except FileExistsError:
        print("User already exists!")
        os.system(f'python3 bin/login.py')
    with open(f'users/{user}/.passfile', 'w') as f:
        f.write(hashlib.sha256(passw.encode()).hexdigest())
    print("\n")
    print("Your account has been created!")
    print("\n")
    print("Now we need to set up your home directory.")
    print("\n")
    print("Please hold on while we create your folders...")
    try:
        os.mkdir(f'users/{user}/Desktop')
    except FileExistsError:
        pass
    with open(f'tmp/cdir', 'w') as f:
        f.write(f'{os.path.abspath(f"./users/{user}")}')
    with open(f'users/{user}/.dshellrc', 'w') as f:
        f.write('theme red')
    print("\n")
    print("Now you will need to pick a hostname")
    print("\n")
    hostname = Prompt.ask("Hostname")
    print("\n")
    with open(f'etc/hostname', 'w') as f:
        f.write(hostname)
    print('The guide is now complete please restart the program.')