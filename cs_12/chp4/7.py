'''Input : (Success)             Output :
Enter an integer: 123               Integer: 123
Enter a string: python

b. Input : (ValueError)             Output :
Enter an integer: abc               Invalid integer input!
Enter a string: python
'''

try:
    num=int(input("enter an integer :"))
    str=input("enter a string :")
    print(int(num))
    print(str.upper())
except ValueError:
    print("Enter number in inetger section !")
else :
    print("All operations successful!")

print('Hello', greeting,'name : ',name)