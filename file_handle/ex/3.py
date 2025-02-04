# Entry 5 user name into txt file using writelines.
with open('us.txt','w') as file:
    for i in range(5):
        name = input("enter user name: ")
        file.write(name + '\n')
