# main_program.py
import m1 as my_module

message = my_module.greet("Alice")
print(message)  # Output: Hello, Alice!

my_dog = my_module.Dog()
print(my_dog.bark()) # Output: Woof!

print(my_module.PI) # Output: 3.14159