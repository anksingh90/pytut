f=open("info.txt","w")
name=input("Enter your name :")
age=input("Enter your age :")
cls=input("Enter your class :")
lst=[name,'\n',age,'\n',cls,'\n']
f.writelines(lst)
f.close()

f=open("info.txt","r")
obj=f.readlines()
print('You have entered below details : ')
for i in obj:
    print(i, end='')
f.close()