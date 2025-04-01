# flashcard application

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+' ( '+self.meaning+' )'

flash = []
print("Welcome to flashcard application \n")

while(True):
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 1 to Exist , Enter 0 to Add  : "))

    if(option == 1):
        break

print("\nYour flashcards")
for i in flash:
    print(">", i)