import csv

my_connection = open("data.csv","r",newline='\r\n')
obj = csv.reader(my_connection)

for i in obj:
    print(i)
