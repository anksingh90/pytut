import random
def asgn():
    lst = ['Layout A', 'Layout B']
    
    for i in range(5):
        layout = random.randint(0,1)
        print(f'User : {i}, Layout Assigned : {lst[layout]}')
asgn()