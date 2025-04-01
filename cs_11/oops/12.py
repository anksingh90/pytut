# Practise Question : H
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I don't speak."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create objects of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Kitty")

# Call the speak method
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")