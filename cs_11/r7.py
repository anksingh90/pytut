# WAP to divide 2 numbers entered by user using try ecept. If number is invalid give error - Invlid number.
# if dividing by Zero - Sorry ! You are dividing by zero

'''a=int(input("enter the first no. :"))
b=int(input("enter the second no. :"))
if a==0 :
    print(" Sorry! The no. is invalid.")
elif b==0 :
    print("Sorry! The no. is invalid.")
elif a!=0 :
    print(a//b)
elif b!=0 :
    print(a//b)'''

'''n=5
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum=sum+j
print(sum)

str="string"
for i in str:
    if i == 'i':
        break
    print(i)'''

# ask user to input a number, if number is positive then add it to sum else break the loop.
# Enter a +ve number, -ve number ends the loop.
sum=0
while True:
    ch = int(input('Enter a +ve number to sum, -ve number ends the loop :'))
    if ch>0:
        print(ch)
        sum=sum+ch
        print(sum)
    elif ch<0:
        break
