'''
Question 3: What's My Position?
Problem: Read story.txt line by line. After reading each line, print the line itself and the cursor's position number returned by tell().
using loop
'''
f=open('story.txt','r')
obj=f.readlines()
for line in obj:
    print(line)
    print('Position : ',f.tell())