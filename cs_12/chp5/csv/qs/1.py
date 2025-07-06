'''
Now, write a Python program to:
- Read the CSV file.
- Calculate the total and average marks for each student.
- Print the result as a formatted table
'''
import csv
myconn=open('stu.csv','r')
obj=csv.reader(myconn, delimiter='\t')
count = 0
for i in obj:
    if count == 0:
        print(', '.join(i),'Avg Marks')
        count = count + 1
    else:
        avg = (int(i[2]) + int(i[3]) + int(i[4]))/3
        print(' '.join(i),' \t ',int(avg))
