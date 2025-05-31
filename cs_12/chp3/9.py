# Write a function create_random_list(), create list of 5 randomly generated number into List : lst.
import random
n=int(input("enter the length of the list :"))
lst=[]
for i in range(n):
    x=random.randint(2,10)
    lst.append(x)
print(lst)