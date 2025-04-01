import random
def dice():
    event=[]
    for i in range(0,3):
        x = str(random.randint(1,6))
        event.append(x)
    print(",".join(event))

dice()