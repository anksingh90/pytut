#create csv file and store 2 students data ( roll no. , name , marks )
import csv
f=open('extension.csv','w')
obj= csv.writer(f, delimiter=',')
stu=input('Enter the no. of students :')
lst=[]
for i in stu:
   roll_no=int(input("Enter the roll no. :"))
   name=input("Enter the name of the student :")
   marks=input("Enter the marks of the student :")
   lst.append([roll_no,name,marks])

obj.writerows([lst])
f.close()