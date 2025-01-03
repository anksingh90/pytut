#create a list of 10 numbers, shuffle the list, then use choice to randomly select the number.
import random
def ppp():
    lst = [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(lst)
    print(random.choice(lst))
ppp()