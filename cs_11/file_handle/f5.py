import os
import csv

file_path = os.path.join("data", "ex.txt")      # Joins path components correctly for different operating systems.
absolute_path = os.path.abspath(file_path)      # Gets the absolute path
print(f"absolute path: {absolute_path}")
if os.path.exists(file_path):
    print(f"File exists: {file_path}")

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
