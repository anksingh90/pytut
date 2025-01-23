class Vehicle:
    def __init__(self,colour,max_speed):
        self.colour = colour
        self.max_speed = max_speed

    def __str__(self):
        return f"colour of vehicle:{self.colour} maximum speed of vehicle: {self.max_speed}"
    
class Car(Vehicle):
    def __init__(self,colour,max_speed,num_doors):
        super().__init__(colour,max_speed)
        self.num_doors = num_doors
    def full_info(self):
        return f"colour: {self.colour};  max_speed: {self.max_speed};  number of doors:{self.num_doors}"

car1 = Car("black", "60m/s", 4)
print(car1.full_info())