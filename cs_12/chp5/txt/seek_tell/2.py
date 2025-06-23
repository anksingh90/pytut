'''
Question 2: Read and Rewind
Problem: Write a script that reads the first line of story.txt, prints it, and then reads and prints 
the entire file from the beginning without closing and reopening it.
'''
f=open('story.txt','r')
obj=f.readline()
print("the first line is :" , obj)
f.seek(0)
obj_1=f.read()
print("the entire file conten is :" , obj_1)
f.close()