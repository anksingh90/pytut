# Practice Question : E , F

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_student(self):
        print(f"Student Name: {self.name}, Roll Number: {self.roll_number}")

# Create an object of the Student class
student = Student("John Doe", 101)
student.display_student()

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()
