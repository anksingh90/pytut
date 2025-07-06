# WAP to number of records present in file - data.csv
import csv
f=open('data.csv','r')
obj=csv.reader(f)
for i in obj:
    obj1=f.readlines()
print(len(obj1))
