'''
Now, write a Python program to:
- Read the CSV file.
- Calculate the total and average marks for each student.
- Print the result as a formatted table
'''
import csv
f=open('stu.csv','r')
obj=csv.reader(f)
for i in obj:
    print(i)