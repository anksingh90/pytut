# Write a Python program to calculate the number of business days between two dates, 
# excluding weekends and holidays.

import datetime

def calculate_business_days_between_dates(start_date, end_date):
    business_days = 0
    for n in range(int ((end_date - start_date).days) + 1):
        date = start_date + datetime.timedelta(n)
        if date.weekday() < 5:
            business_days += 1
    return business_days

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 1, 31)
print("Number of business days between dates: ", calculate_business_days_between_dates(start_date, end_date))
