class Car:
    def __init__(self,c_brand,c_model,c_year):
        self.brand = c_brand
        self.model = c_model
        self.year = c_year
    
    def display_info(self):
        return f"The car is model {self.model} of {self.brand} of the year:{self.year}"
    
c1 = Car("mahindra","BE6",2019)
print(c1.display_info())