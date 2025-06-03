'''
 Default Argument Function
 Create a function calculate_area(length, width, unit="square meters") that calculates the area of a rectangle. 
 The function should return the area along with the unit.
'''

def calculate_area(length , width , unit = 'sq mtr'):
    area=length*width
    a=print(area , "sq. m") # 10 sq mtr
    return a

length=10
width=4.5
calculate_area(length,width)