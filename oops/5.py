# Create an Electric Car Class that inherits from Class Car and have additional attribute - battery size

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

mm = Electric_car('Mahindra', 'Be 6', '80 kWh')
print(mm)

#c1 = Car('Tata', 'Safari')
#print(c1.brand, c1.model) 
#print(c1.full_name())