# calculate the numbers of capital / small / numbers in the txt file. Also check the number of vowels.
a_count=0
d_count=0
l_count=0
f=open("data.txt","r")
obj=f.read()
for i in obj:
    if i.isupper()==True:
        a_count+=1
    elif i.isdigit()==True:
        d_count+=1
    elif i.islower()==True:
        l_count+=1
print(i)
print(a_count)
print(d_count)
print(l_count)
f.seek(0)
print(obj)
v_count=0
vowels="AEIOUaeiou"
for i in obj:
    if i in vowels:
        v_count+=1
print(v_count)
f.close()