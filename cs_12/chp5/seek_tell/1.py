'''
open file in read mode 
i.   print present position
ii.  move 5 byte forward
iii. confirm position using tell().
iv.  read 10 bytes of data and print position using tell()
'''
f=open('story.txt','r')
f.read(5)
f.tell()
f.read(10)
print(f.tell())
