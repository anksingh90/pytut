count = 0 
with open('ex.txt','r') as file:
    read_mode = file.read().split()
    print(len(read_mode))
    for i in read_mode:
       if i.isspace():
            count+=1
print(count)