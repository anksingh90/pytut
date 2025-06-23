import csv

f=open('extension.csv','w')

obj= csv.writer(f, delimiter=',')
obj.writerow(['hello','python','world'])

f.close()