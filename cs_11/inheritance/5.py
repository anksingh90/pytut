# Write a program where you have a base class Vehicle with a method start_engine. 
# Create two derived classes Car and Bike that override the start_engine method.
class Vehicle:
    def start_engine(self):
        print("engine started.")
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

vehicles = [Vehicle(), Car(), Bike()]
for i in vehicles:
    i.start_engine()