# Enter 5 entry from user into txt file
with open('us.txt','w', newline='') as file:
    for i in range(5):
        name = input("enter name: ")
        file.write(name + '\n')
