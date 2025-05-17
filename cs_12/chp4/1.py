try:
    x=int(input("enter no. 1 :"))
    y=int(input("enter no. 2 :"))
    z=x/y
    print(z)
except ZeroDivisionError:
    print("number can't be divided by 0")
except ValueError:
    print("value missing")
    