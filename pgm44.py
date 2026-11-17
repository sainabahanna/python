

import datetime
import time

now = datetime.datetime.now()

print("current date and time:", now)
print("current year:", now.year)
print("month of the year:", now.month)
print("weekday no of year:", now.strftime("%u"))
print("day of year",now.strftime("%j"))
print("day of month",now.day)
print("day of week",now.weekday())
