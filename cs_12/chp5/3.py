#count the no. of words present in the file.
f=open('data.txt','r')
obj=f.read()
word=obj.split()
print(len(word))