#create a electric car classs that inherits from class car and have additional attributes: batterysize.
class Car:
    def __init__(self,u_brand,u_model):
        self.brand = u_brand
        self.model = u_model

    def c_carname(self): 
        c_car = f"Manufacturer : {self.brand} & Model : {self.model} "
        return c_car

class Electric_car(Car): # inheritance
    def __init__(self,u_brand,u_model,u_battery_size):
        super().__init__(u_brand, u_model)
        self.battery_size = u_battery_size
    def __str__(self): 
        c_car = f"Manufacturer : {self.brand} & Model : {self.model} "
        return c_car

e1 = Electric_car("mahindra",'BE6',"80 kwh")
print(e1.c_carname(),e1.battery_size)
print(e1)