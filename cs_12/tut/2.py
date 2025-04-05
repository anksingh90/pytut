# A program that input an integer in range 0 - 999, then print if the integer is entered is a 1 / 2 / 3 digit number.

num = int(input("Enter an integer in range 0 - 999: "))
if num < 0 or num > 999:
    print("Number is out of range.")
else:
    if num < 10:
        print("The number is a 1-digit number.")
    elif num < 100:
        print("The number is a 2-digit number.")
    else:
        print("The number is a 3-digit number.")
# The program checks if the number is in the range of 0 to 999 and then determines the number of digits in the number.