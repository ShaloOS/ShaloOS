import os
print(f'Current uptime is {os.popen("uptime").read()}')