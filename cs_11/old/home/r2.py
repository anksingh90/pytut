#define a rolled dice(n) fun0ction tht simulates the roll of n dice and returns ordered list.
#for example, rolled d0ice (3)=2,5,1. and returns the list[1,2,5]
import random

def rolled_dice(num):
    lst=[]
    for i in range(num):
        lst.append(random.randint(1,6))
    lst.sort(reverse=False)
    return lst
    
num = random.randint(1,6) 
print(rolled_dice(num))
