# flashcard quiz
import random

class flashcard:
    def __init__(self):
      
        self.fruits={'apple':'red', 'orange':'orange', 'watermelon':'green', 'banana':'yellow'} #dictionary
        
    def quiz(self):
        while (True):          
            fruit, color = random.choice(list(self.fruits.items()))           
            print("What is the color of {}".format(fruit))
            user_answer = input()
            
            if(user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")
                
            option = int(input("enter 0 , if you want to play again : "))
            if (option):
                break

print("Welcome to fruit quiz! /n ")
fc=flashcard() #object
fc.quiz() # initiating quiz function