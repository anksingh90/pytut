# print output from data.csv in form of comma separated values, instead of list.

import csv
f=open('data.csv','r')
obj=csv.reader(f)
for i in obj:
    print(','.join(i))