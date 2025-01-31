import random as rm

count = 0 
with open('ex.txt','r') as file:
    read_mode = file.readlines()
    print('read_mode',read_mode)
    file.seek(0)
    read1 = file.read()
    file.seek(0)
    print('read1',read1)
    read2 = file.readline()
    print('read2',read2)