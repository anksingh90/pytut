import csv

f=open('extension.csv','r')

obj= csv.reader(f, delimiter=',')
print(obj)
for i in obj:
    print(i)

f.close()