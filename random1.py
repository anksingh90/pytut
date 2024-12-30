#create a 8 alphnumeric password using random. 65 - 90 : A - Z, 97 - 122 : a - z
import random
a = str(random.randint(0,9))
b = str(random.randint(0,9))
c = chr(random.randint(65,90))
d = chr(random.randint(65,90))
e = chr(random.randint(65,90))
f = chr(random.randint(97,122))
g = chr(random.randint(97,122))
h = chr(random.randint(97,122))
pswd = [a,b,c,d,e,f,g,h]
random.shuffle(pswd)
print("".join(pswd))
