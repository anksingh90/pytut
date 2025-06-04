#wap that reads a txt file and displays those lines which begin with the word "THE"
f=open("data.txt","r")
obj=f.readlines()
for i in obj:
    x=i.split()
    if x[0]=='The':
        print(x)
