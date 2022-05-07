from rich.prompt import Prompt
import hashlib,os
user = Prompt.ask("Username")
if not user in os.listdir('users/'):
    os.mkdir(f'users/{user}')
    password = Prompt.ask("Password",password=True)
    with open(f'users/{user}/.passfile', 'w') as f:
        f.write(hashlib.sha256(password.encode()).hexdigest())
        print("You made the account called {}!".format(user))
    with open(f'users/{user}/.dshellrc', 'w') as f:
        f.write('theme red')
    try:
        os.mkdir(f'users/{user}/Desktop')
    except FileExistsError:
        pass