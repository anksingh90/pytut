# flashcard application

class FlashCard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word}({self.meaning})"

flshcrds = []
print("Welcome to flashcard game!!")

while(True):
    word = input("Enter a word : ")
    meaning = input("Enter meaning of word : ")
    f1 = FlashCard(word, meaning)
    flshcrds.append(f1)

    ch = input("do you want to continue? Y/N ")
    if ch.lower() == 'n' :
        break

for i in  flshcrds:
    print(i)