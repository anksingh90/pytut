# Modify the Car class to encapsulate the brand attribute, making it private, and 
# provide a getter method for it.

class Car():
    def __init__(self, brand,model):
        self.__brand = brand # brand is private attribute
        self.model = model
    def full_name(self):
        return f"{self.__brand}, {self.model} "
    
    def get_brand(self):
        return self.__brand + '!'  # method used to access brand

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_ev = ElectricCar('Tesla', 'Model S', '85 kWh') # object

#print(my_ev.__brand)
print(my_ev.get_brand())