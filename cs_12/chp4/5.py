'''
1. Ask the user to enter an integer. If the user enters something that cannot be converted
to an integer (e.g., text), print an error message.
Input :                         Output : 
Enter an integer: 42            You entered: 42
Enter an integer: hello         Invalid input! Please enter a number
'''
try:
    num=int(input("enter an integer :"))
    num1=int(input("enter an interger :"))
    print(num)
    print(num1)
except :
    print('Invalid input! Please enter a number')

