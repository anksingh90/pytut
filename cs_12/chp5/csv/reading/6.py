# read data from data.csv and skip the header while print the rest of data.
import csv
f=open("data.csv",'r')
obj=csv.reader(f)
counter = 0
for i in obj:
    if counter == 0:
        counter = counter + 1
        continue
    else:
        print(i)
