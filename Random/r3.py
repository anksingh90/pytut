import random

def character():
    names = ['Warrior', 'Mage', 'Rogue']
    weapons = ['Sword', 'Staff', 'Dagger']

    for i in range(0,1):
        r_name = random.randint(0,2)
        r_weapons = random.randint(0,2)
        r_name, r_weapons = names[r_name],weapons[r_weapons]
    return r_name, r_weapons

na, we = character() # calling function
print(f'The character : {na}, has weapon : {we}')