'''
Count Characters : Write a program to count the number of characters (including spaces and newlines) in a file
'''
f=open('data.txt','r')
data=f.read()
count=0
for i in data:
    if i.isalpha:
        count=count+1
        print(count)
f.close()