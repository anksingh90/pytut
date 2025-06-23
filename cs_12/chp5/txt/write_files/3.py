#create a file with input details - roll no. , name , marks of student and score in marks.txt using write function.
f=open('marks.txt','w')
n=int(input("enter the no. of stu :"))
for i in range(n):
    name=input("enter the name :")
    roll_no=input("enter the roll no. :")
    marks=input("enter the marks of the student :")
    data = f"Roll No : {roll_no} \t Name : {name} \t Marks : {marks} \n"
    f.write(data)

'''    f.write(name+'\t')
    f.write(roll_no+'\t')
    f.write(marks+'\t'+'\n')
'''
print('info added to the file !')
f.close()