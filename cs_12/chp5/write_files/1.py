# first program - write files

myconn = open('data.txt','w')
for i in range(5):
    name = input('Enter name : ')
    myconn.write(name)

myconn.close()
