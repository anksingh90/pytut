# Create a list lst and input 5 numbers using f-string and for loop

lst=[]
for i in range(5):
    num=int(input("enter the number :"))
    lst.append(num)
    n = f"Roll_{num}"
    print(n)

for i in lst:
    print(f" Value in the list : {i} ")
