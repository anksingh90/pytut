'''
Uppercase Conversion : Read a file and print all lines in uppercase.
'''
f=open('data.txt','r')
data=f.read()
print(data.upper())
f.close()