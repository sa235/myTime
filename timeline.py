import datetime

now = datetime.datetime.now()
 
then = datetime.datetime(2020, 11, 2)
 
# Кол-во времени между датами.
delta = then - now 
 
print("Delta day: ", delta.days) # 38
#print("Delta month: ", delta.month) # 1131

seconds = delta.total_seconds()
hours = seconds // 3600
 
print(hours) # 186.0
 
minutes = (seconds % 3600) // 60
print(minutes) # 13.0