'''
Write a program to generate 6 digit OTP using for loop and random.randint(a,b) statement once.
'''
import random
lst=[]
for i in range(6):
    x=random.randint(0,9)
    lst.append(x)
print(lst)