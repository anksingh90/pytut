#write the py function that reads no. of chars from file and give the count.
with open('ex.txt','r') as file:
    read_mode = file.read()
count = 0
for i in read_mode:
    print(i, end='')
    count = count + 1
    if count == 50:
        break
print()