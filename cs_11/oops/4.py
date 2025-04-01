# Add a method (new functionality) to Class Car, display complete name of car (model + brand).

class Car:
    def __init__(self, u_brand, u_model):
        self.brand = u_brand
        self.model = u_model

    def full_name(self): 
        f_name = f"Manufacture : {self.brand}, Model : {self.model}"
        return f_name

c1 = Car('Tata', 'Safari')
print(c1.brand, c1.model) 
print(c1.full_name())