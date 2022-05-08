from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print("The current time is:", dt_string)	
