class Dog:
    def __init__(self,d_name,d_breed,d_age):
        self.name = d_name
        self.breed = d_breed
        self.age = d_age
    
    def bark(self):
        b = "woof"
        return b
    
    def description(self):
        d_esc = f"{self.name}is a {self.age} year old {self.breed}"
        return d_esc

dog1 = Dog("coco","husky","2")
print(dog1.bark())
print(dog1.description())