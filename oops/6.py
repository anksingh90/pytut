# The error you're seeing is because you're printing the object directly,
# which by default shows the object's memory address
# To print object value, you need to define __str__ method in your Electric_car class.

class Car:
    def __init__(self, u_brand, u_model):
        self.brand = u_brand
        self.model = u_model

    def full_name(self): 
        f_name = f"Manufacture : {self.brand}, Model : {self.model}"
        return f_name

class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def __str__(self):
        return f"{self.full_name()}, Battery Size: {self.battery_size}"

mm = Electric_car('Mahindra', 'Be 6', '80 kWh')
print(mm)