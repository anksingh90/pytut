
def prime_num(num):
    if num<2:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            print('Not Prime number')
            return False # Not Prime number
    print('Prime Number')
    return True # Prime Number

num=int(input("enter the no."))
x = prime_num(num) # accepting True or False

if x == True: # if x == True
    print(num,'Prime Number')
else:
    print(num,'Not Prime Number')