'''
Read the file line by line and print each line with a line using readline
'''
f=open("data.txt",'r')
while True:
    data=f.readline()
    if not data:
        break
    else:
        print(data)
f.close()
