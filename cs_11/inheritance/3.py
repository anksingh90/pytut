class Animal:
    def make_sound(self):
        print('Animal')

class Dog():
    def make_sound(self):
        print('Dog!')

animals = [Animal(), Dog()]
for animal in animals:
    animal.make_sound()