f=open("data.txt","r")
x=f.readlines()

for i in x :
    print(i,end='')
print()
f.close()