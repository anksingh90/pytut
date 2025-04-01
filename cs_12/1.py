# WAP to print '*' in acending order of 1 to 5.

'''n=4
for i in range (1,n+1):  # range(start point, end point)
    for j in range(i):
        print('*',end='')
    print('')

#wap to find 1st and last chr of a word.

word="hello"
print(word[0])
print(word[-1])

# Write a program to perform these action - 
# 1. check is string is empty or not
# 2. calculate the lenght of a string 
# 3. print in reverse order

wrd = 'Earth'
if len(wrd)<0:
    print("the given string is empty")
else:
    print(len(wrd))
    print(wrd[::-1])
'''

# String = Hello World!
# 1. print first 3 and last 3 character of string.
# 2. print every alternate character from string.
# 3. print string removing first and last characters of string.
# print first 3 and last 3 character of string using loop.

'''str="hello world!"

print('First 3 character  : ', end='') #printing first 3 charac of string.
for i in range(0,3):
    print(str[i],end ='')
print('')

print('last 3 character : ', end='')
for i in range(-3,-1):
    print(str[i],end ='')
print('')

print('alternate characters of str : ' , end='')
print(str[::2])

print(' str without first and last 3 chr : ' , end='')
print(str[3:9])'''

#wap to count the numbers of vowels in the string
count=0
str="hello world"
x="aeiou"
for i in str:
    if i in x:
        count=count+1
print(count)

