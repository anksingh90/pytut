# input 3 students name into file - data.txt, also once save give confirmation to user

f=open('data.txt','w')
stu_lst=[]
for i in range(3):
    stu=input("enter the name of student :")
    stu_lst.append(stu+'\n')

f.writelines(stu_lst) # writing file into data.txt
print("info added !")
f.close()
