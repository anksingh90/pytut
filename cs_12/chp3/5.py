# write a program to generate number between 10 & 50
import random

print("WELCOME TO THE GAME !")
a=input("enter Y/y to start the game :")

if 'y' in a.lower():
    roll=random.randint(1,6)
    print("The number on the dice is :" , roll)
else:
    print('Invalid Resposne !')