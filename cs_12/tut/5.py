# Implement a Python program to calculate the sum of the first n natural numbers using a while loop.

n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of first", n, "natural numbers is:", sum)

#  - Write a Python program to print the multiplication table of a given number using a for loop.

num = int(input("Enter a number: "))
print("Multiplication table of", num, "is:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#  - Create a Python program to find the factorial of a number using a while loop.

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial of", num, "is:", fact)

#  - Write a Python program to print the Fibonacci sequence up to a given number of terms.

n = int(input("Enter the number of terms: "))
print("Fibonacci sequence up to", n, "terms is:")
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#  - Implement a Python program to check if a number is prime or not.

num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")

#  - Write a Python program to reverse a given number.

num = int(input("Enter a number: "))
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reverse of the number is:", reversed_num)

#  - Write a python program to accept two integers upto 2 digit and then swap both.

# Get two integers from the user
num1 = int(input("Enter the first integer (up to 2 digits): "))
num2 = int(input("Enter the second integer (up to 2 digits): "))

# Validate input (ensure numbers are within 2-digit range)
while not (0 <= num1 <= 99 and 0 <= num2 <= 99):
    print("Both numbers should be between 0 and 99.")
    num1 = int(input("Enter the first integer (up to 2 digits): "))
    num2 = int(input("Enter the second integer (up to 2 digits): "))

# Swap the numbers
temp = num1
num1 = num2
num2 = temp

#num1, num2 = num2, num1

# Print the swapped numbers
print("After swapping:")
print("First integer:", num1)
print("Second integer:", num2)

#  - Write a Python program to count the number of digits in a given number.

num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Number of digits in the number is:", count)