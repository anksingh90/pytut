# Read the content of a file named data.txt and print it to the console.

f=open("data.txt",'r')
data=f.read()
print(data)
f.close()