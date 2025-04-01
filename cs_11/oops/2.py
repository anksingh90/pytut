# Create a Class - Car with attributes : Brand , Model. Then create an instance of this class.

class Car:
    def __init__(self, u_brand, u_model):
        self.brand = u_brand
        self.model = u_model

c1 = Car('Tata', 'Safari')
print(c1.brand)
print(c1.model)

# this is form with basic information
# we should add few more additional functionalities