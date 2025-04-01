import random
def event():
    lst = []
    c_lst = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
    for i in range(0,3):
        x = random.randint(0,6)
        lst.append(c_lst[x])
    print(lst)

event()