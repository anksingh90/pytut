# Create an ElectricCar class that inherits from the Car class and has an additional 
# attribute battery_size
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def full_name(self):
        return f"{self.model} of brand {self.__brand}."
    def get_brand(self):
        return f"brand of car: {self.__brand}"
    
class Electric_Car(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

e1 = Electric_Car("tata","r8",2)
print(e1.get_brand())
print(e1.get_brand())
