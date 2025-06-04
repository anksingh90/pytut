#read data.txt and display count of numbers present in file. 
f=open('data.txt','r')
obj=f.read()
d_count=0

for i in obj:
    if i.isdigit():
        d_count = d_count + 1

print(d_count)
f.close()