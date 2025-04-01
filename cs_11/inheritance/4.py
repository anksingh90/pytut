# Create a program with a base class Shape that has a method area. 
# Implement two derived classes Circle and Square and override the area method in 
# each of them.

class Shape:
        def area(self):
             pass

class Circle(Shape):
    def __init__(self,size):
        self.size = size
    def area(self):
        return 2*3.14*self.size

class Square(Shape):
    def __init__(self,size):
        self.size = size
    def area(self):
        return self.size*self.size

area = [Circle(5), Square(4)]
for i in area:
    print(i.area())