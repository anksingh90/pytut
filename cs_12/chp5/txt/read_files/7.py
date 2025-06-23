'''Line Count : count the the no. of lines present in the file'''

f=open('data.txt','r')
obj=f.readlines()
count=0
for i in obj:
    count=count+1
    print(count)
f.close()