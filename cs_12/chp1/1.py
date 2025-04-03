# 1. Write a Python program that takes an integer as input and prints whether it is a prime number or not. Use a for loop and if-else statements.

num = int(input("Enter an integer: "))

if num <= 1:
    print('number is not a prime number !')

# formula :  range(2, sqrt(num)+1)
n = int(num**0.5)
for i in range(2, n + 1):
    print(i,n, num)
    if num % i == 0:
        flag = False
    flag = True

if flag == True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")