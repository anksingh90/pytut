def a_circle():
    #pi*r*r
    r=int(input("enter the value of radius:"))
    a_circle = 3.14*r*r
    print(a_circle)

def C_circle():
    #2*pi*r
    r1=int(input("enter the value of radius:"))
    C_circle = 2*3.14*r1
    print(C_circle)
print ("press 1 : area of circle")
print ("press 2 : circumference of circle")

ch = input("enter your choice :")

if ch == '1':
    a_circle()
elif ch == '2':
    C_circle()