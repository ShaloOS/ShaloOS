from rich.prompt import Prompt
import shutil,os
a = Prompt.ask("What user would you like to delete")
if os.path.exists(f'users/{a}'):
    b = Prompt.ask("Are you sure you want to delete {}".format(a),default="n",choices=["y","n"])
    shutil.rmtree(f'users/{a}')
    print("User deleted!")
else:
    print("User does not exist!")
    print("\n")