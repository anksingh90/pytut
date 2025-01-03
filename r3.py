#
import random
import string
def gen_pswd():
    str_ch = string.ascii_letters + string.digits + string.punctuation
    pswd = []
    len = random.randint(8,16)
    for i in range(1,len):
        x = random.choice(str_ch)
        pswd.append(x) 
    print("".join(pswd))   

gen_pswd()
