# Write a function to print the current time in 12-hour format.

import datetime

def print_current_time():
    current_time = datetime.datetime.now()
    print('Current date : ',current_time)
    print("Current Time (12-hour format): ", current_time.strftime("%I:%M %p"))

print_current_time()