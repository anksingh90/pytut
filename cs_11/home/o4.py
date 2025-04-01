class Rectangle:
    def __init__(self,r_length,r_width):
        self.length = r_length
        self.width = r_width
    def area(self):
        area = self.length * self.width
        return area
    def perimeter(self):
        perimeter =2*(self.length + self.width)
        return perimeter
    
rec1 = Rectangle(5,3)
print(rec1.perimeter())
print(rec1.area())