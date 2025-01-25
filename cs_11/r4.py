# accept number from user and check if it is odd or even.

'''a=int(input("enter the number :"))
if a%2==0 :
    print("the number is even.")
else:
    print("the number is odd.")'''

'''a = int(input("enter number between 1-5"))
if (a==1):
    print("you entered press 1")
elif (a==2):
    print("you entered press 2")
elif (a==3):
    print("you entered press 3")
elif (a==4):
    print("you entered press 4")
elif (a==5):
    print("you entered press 5")
else:
    print("you entered invalid choice")'''

'''temp=0
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
temp=a
a=b
b=temp
print(a)
print(b)'''

'''a=int(input("enter the salary of employee :"))
if (a>=0 and a<=10):
    print ("taxation is 0%")
elif (a>10 and a<=15) :
    print ("taxation is 10%")
elif (a>15 and a<=20) :
    print ("taxation is 15%")
elif (a>20 and a<=25) :
    print ("taxation is 20%")
elif (a>25 and a<=30) :
    print ("taxation is 25%")
elif (a>30 and a<=100) :
    print ("taxation is 30%")'''
'''a=5
for i in range (0,10):
    print(a*i)'''

'''str=("hello world !")
for ch in str :
    print(ch)'''

a=int(input("enter the no. :"))
permutation = 1
b=input("do you want to continue or exit ")
if a > 0:
    for i in range(1, a+1):
        permutation = permutation * i
    print(permutation)
else:
    print('incorrect value')

