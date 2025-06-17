# Write a Python program to calculate the difference between two dates.

import datetime

def calculate_date_difference():
    date1 = datetime.date(2024, 1, 1)
    date2 = datetime.date(2024, 1, 15)
    difference = date2 - date1
    print('Date 1 : ',date1)
    print('Date 2 : ',date2)
    print("Difference between dates: ", difference.days, " days")

calculate_date_difference()