import random
class FlashCard:
    def __init__(self):
        self.fruits = {'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}

    def quiz(self):
        key,value = random.choice(list(self.fruits.items()))
        u_value = input(f"what is the colour of {key}: ")
        if u_value == value : 
            print("CORRECT ANSWER")
        if u_value != value:
            print("INCORRECT ANSWER")

f1 = FlashCard()
f1.quiz()