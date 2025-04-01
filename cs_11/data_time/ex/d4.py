# Write a Python program to parse a string in the format "YYYY-MM-DD HH:MM:SS" into a datetime object.

import datetime

def parse_string_to_datetime():
    date_string = "2024-01-01 12:00:00"clear
    
    dt = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print("Parsed DateTime Object: ", dt)

parse_string_to_datetime()