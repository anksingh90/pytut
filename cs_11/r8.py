# sum all the positive number entered by user, if any negative number entered should terminate the loop.
# once loop terminated, print the total sum.

'''sum=0
while True:
    a=int(input("enter any positive number :"))
    if a>0:
        sum=sum+a
    elif a<0:
        break
print('total sum:',sum)'''


#sum=(2**n)-1 and display 10 numbers by taking user input

'''n=int(input("Enter the number of elements :"))
for i in range (1,n+1):
    m=2**i -1
    print(m)'''

n=6
for i in range(1,n):
    for j in range(i,0,-1):
        print(j,' ', end='')
    print('')
