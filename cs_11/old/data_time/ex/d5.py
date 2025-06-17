# Create a timedelta object that represents a duration of 3 days, 2 hours, and 1 minute, and 
# add it to a datetime object.

import datetime

def add_timedelta_to_datetime():
    dt = datetime.datetime.now()
    td = datetime.timedelta(days=3, hours=2, minutes=1)
    new_dt = dt + td
    print("New DateTime Object: ", new_dt)

add_timedelta_to_datetime()