import datetime

now = datetime.datetime.now()
 
then = datetime.datetime(2020, 11, 2)
 
# Кол-во времени между датами.
delta = then - now 
 
print("Delta day: ", delta.days) # 38
#print("Delta month: ", delta.month) # 1131

seconds = delta.total_seconds()
hours = seconds // 3600
 
print("hours", hours) # 186.0
 
minutes = (seconds // 60)
print("minutes", minutes) # 13.0

week = datetime.datetime.now().isocalendar()[1]
print("week ", week) # 13.0