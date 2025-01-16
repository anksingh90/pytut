# write a function that fills a list with numbers.
import random

def lstrandom():
    lst=[]
    for i in range (5):
        lst.append(random.randrange(10,100))
    print (lst)

lstrandom()