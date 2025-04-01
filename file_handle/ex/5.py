# Make 2 function : write / read to simultaneously write and read as per user input.
def write():
    with open('us.txt','w') as file:
        user_inpt = input("enter input: ")
        file.write(user_inpt)
def read():
    with open('us.txt','r') as file:
        read_mode = file.read()
        print(read_mode)

write()
read()