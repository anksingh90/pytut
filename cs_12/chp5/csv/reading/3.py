# Print content of file data.csv excluding header.
import csv
f=open('data.csv','r')
obj=csv.reader(f)
for i in obj:
    #print(i)
    obj1=f.readlines(0)
print(obj1)