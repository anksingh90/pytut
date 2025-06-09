'''
Count Words : Write a program to read a text file and count the number of words in it.
'''
f=open('data.txt','r')
data=f.read()
obj=data.split()
print(len(obj))
f.close()

