### DATES ###

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now)

timestamp = now.timestamp()
print(timestamp)

year_2024 = datetime(2024,1,1)

def print_date (date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date)

print_date(now)


from datetime import time

current_time = time(15, 27, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2024, 1, 27)
current_date_two = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

print(current_date_two)

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)



from datetime import timedelta

init_timedelta = timedelta(200, 100, 100, weeks = 35)
stop_timedelta = timedelta(400, 400, 400, weeks = 11)

print(stop_timedelta - init_timedelta)
print(stop_timedelta + init_timedelta)