#open a file in read mode and count total no. of lines present in file
count = 0
with open('ex.txt','r') as file:
    read_mode = file.readlines()
print(len(read_mode))
for i in read_mode:
    print(i)
    count+=1
print(count)