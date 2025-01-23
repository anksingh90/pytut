# Create an ElectricCar class that inherits from the Car class and has an additional attribute 
# battery_size.

class Car():
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand}, {self.model} "

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_ev = ElectricCar('Tesla', 'Model S', '85 kWh') # object
print(my_ev.model)
print(my_ev.battery_size)
print(my_ev.full_name())