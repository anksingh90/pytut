# Enter user name in txt file
with open('us.txt','w') as file:
    name = input("enter name: ")
    read_mode = file.write(name)
