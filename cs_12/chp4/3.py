'''try:
    a=k
    b=y
    c=a//b
    print(c)
except:
    print("an error has occured")'''

try:
    num1=int(input("enter 1st no. :"))
    num2=int(input("enter 2nd no. :"))
    x=num1/num2
    print(x)
except ZeroDivisionError:
    print("number cannot be divided by 0 !!")
except TypeError:
    print("characters are not allowed !!")
finally:
    print("code executed !")