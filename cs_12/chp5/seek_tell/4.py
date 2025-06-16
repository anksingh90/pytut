'''
Question 4: The Bookmarker
Problem: Read story.txt and store the starting position of the second line. Then, read the rest of the file. 
Finally, use the stored position to go back and print only the second line again.

Hint:
Read the first line to move the cursor past it.
Immediately call tell() to get the starting position of the second line and save it in a variable.
Continue reading the file.
Use seek() with your saved variable to jump back.
'''

f=open('story.txt','r')
f.readline() # read line 1
b_pos=f.tell() # save position of line 2
print('bookmark position :',b_pos)
f.read() # reading entire file
print('reading the entire file')
print('moving to the position',b_pos)
a=f.seek(b_pos)
print('printing the 2nd line :' , f.readline())