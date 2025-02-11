class Animal:
    def __init__(self,a_name):
        self.name = a_name
    def speak(self):
        print("I am human.")

class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
dog = Dog("coco")
cat = Cat("meow")

print(dog.speak())
print(cat.speak())