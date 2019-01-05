# Full program

import datetime

date = datetime.datetime.now()
date.year
date.month
weekNumber = date.today().isocalendar()[1]
date.day

print(date)
print(date.year)
print(date.month)
print(weekNumber)
print(date.day)
