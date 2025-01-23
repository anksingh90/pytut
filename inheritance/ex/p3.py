# Create a Vehicle class with attributes color and max_speed. Then, create a Car class that 
# inherits from Vehicle and adds an attribute num_doors.

class Vehicle:
    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed

    def __str__(self):
        return f"Vehicle (color={self.color}, max_speed={self.max_speed})"

class Car(Vehicle):
    def __init__(self, color, max_speed, num_doors):
        super().__init__(color, max_speed)  # Call the Vehicle constructor
        self.num_doors = num_doors

    def __str__(self):
        return f"Car (color={self.color}, max_speed={self.max_speed}, num_doors={self.num_doors})"

vehicle = Vehicle("Red", 120)
print(vehicle)
car = Car("Blue", 150, 4)
print(car)