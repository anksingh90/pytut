# Read only the first line of data.txt and display it.

f=open("data.txt",'r')
data=f.readline()
print(data)
f.close()