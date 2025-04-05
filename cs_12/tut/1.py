# Dynamic Typing
print('Dynamic Typing')
x = 10
print('Value of x : ',x)
x = '‘hello’'
print('New Value : ',x)

# Mutable & Un-Mutable Types
print('\nMutable & Un-Mutable Types')
my_list = [1, 2, 3]
print('Original List : ',my_list)
my_list[0] = 10  # my_list is now [10, 2, 3]
print('Edited List : ',my_list)

my_string = "hello"
# my_string[0] = 'H'  # Uncommenting this line will cause a TypeError

# Type Casting
print('\nType Casting')
b = 10.2
print('Value of b : ',b,type(b))
b = int(b)  # Type Casting
print('Value of b : ',b,type(b))