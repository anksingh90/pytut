# reading data from data.csv file.

import csv

f=open('data.csv','r')

obj= csv.reader(f, delimiter=',')
print(obj)
for i in obj:
    print(i)

f.close()