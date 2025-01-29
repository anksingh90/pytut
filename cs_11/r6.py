
'''x = 5
for i in range(x+1,1,-1):
    for j in range(i):
        print('*', end='')
    print(i)'''

n = 5
sum = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        sum = sum + j
print(sum)