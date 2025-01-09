# Create a Class - Car with attributes : Brand , Model. Then create multiple instance of this class.

class Car:
    def __init__(self, u_brand, u_model):
        self.brand = u_brand
        self.model = u_model

c1 = Car('Tata', 'Safari')
print(c1.brand, c1.model)

c2 = Car('Mahindra', 'Thar')
print(c2.brand,c2.model)