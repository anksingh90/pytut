# write a program that multiplies two numbers without using the * operator, using repeated addition

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
result = 0
for i in range(n2):
    result += n1
print(f"The result of {n1} * {n2} is: {result}")
# The above code works for positive numbers only