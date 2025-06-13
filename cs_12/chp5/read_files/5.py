# read data from data.txt file and print output in upper case

f=open("data.txt",'r')
obj=f.read()
#print('Printing the value in file : ',obj.upper())
f.close()

f=open("data.txt",'r')
obj1=f.readlines()
print("no. of lines present in the file are :" , len(obj1))
f.close()