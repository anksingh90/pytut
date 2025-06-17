import random
def gen_pswd():
    pswd = []
    for i in range(6):
        x = str(random.randint(0,9))
        pswd.append(x)
    
    print("".join(pswd))

def ch_pswd():
    pswd = []
    a = [0,1,2,3,4,5,6,7,8,9]
    for i in range(6):
        x = str(random.choice(a))
        pswd.append(x)
    print("".join(pswd))

#gen_pswd()
ch_pswd()