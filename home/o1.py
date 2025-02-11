# create a class - car with attributes: brand,model. then create an instance of the class.
#add a method to class car, display complete name of car.

class Car:
    def __init__(self,u_brand,u_model):
        self.brand = u_brand
        self.model = u_model

    def c_carname(self): # inheritance
        c_car = f"Manufacturer : {self.brand} & Model : {self.model} "
        return c_car

c1 = Car('tesla', 'model S')
c2 = Car('TaTa','byebye')
print(c1.c_carname())

#print(c1.brand)
#print(c2.brand,c2.model)
