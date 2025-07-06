# WAP to read data from file - data.csv and copy its content into a new list - lst. Print data of lst.

import csv
f=open('data.csv','r')
obj=csv.reader(f)
lst=[]
for i in obj:
    lst.append(i)
print(lst)
f.close()
