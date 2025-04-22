'''
Write a Python program to demonstrate how variable assignment and modification affect the memory addresses of variables.
Assign variable a value 10
Copy value from a into b.
Print the memory addresses of a and b using the id() function
Modify the value of b using b = b + 4 and print address again.
'''
a = 10
b = a

# Print the memory addresses of a and b
print(f"Initial Values:")
print(f"a = {a}, Memory Address: {id(a)}")
print(f"b = {b}, Memory Address: {id(b)}")

b = b + 4

# Print the memory addresses of a and b after modification
print(f"\nAfter Modification:")
print(f"a = {a}, Memory Address: {id(a)}")
print(f"b = {b}, Memory Address: {id(b)}")