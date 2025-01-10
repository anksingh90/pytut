# Practice Question : A

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof!")

    def description(self):
        print(f"{self.name} is a {self.age}-year-old {self.breed}.")

fido = Dog("Fido", "Golden Retriever", 3) # Object created for class Dog
fido.bark()  # Output: Woof!
fido.description()  # Output: Fido is a 3-year-old Golden Retriever.