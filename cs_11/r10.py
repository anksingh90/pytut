'''
# count number of char values in string and print count

a=input("enter the word :")
count = 0
for i in a:
    if i.isalpha()==True:
        count = count + 1
print(count)
print(len(a))

# accept string from user and convert it into capitalize letters

str=input("enter the word :")
print(str.upper())
str1=str.upper()
print(str1.lower())

#wap that reads a line and print no. of uppercase / lowercase / alphabets / digits

str=input("write a line :")
u_count = 0
l_count = 0
a_count = 0
d_count = 0
s_count = 0
for i in str:
    if i.isupper():
        u_count = u_count + 1
    elif i.islower():
        l_count = l_count + 1
    elif i.isalpha():
        a_count = a_count + 1
    elif i.isdigit():
        d_count = d_count + 1
    elif i.isspace():
        s_count = s_count + 1
print(u_count)
print(l_count)
print(a_count)
print(d_count)
print(s_count)
print("abcd"*3)

# slicing of string

x = 'HelloWorld'
print(x)
x1 = x[2:]
print(x1)
x2 = x[:6]
print(x2) 

# count number of vowels in a string.

st = 'Hello World'
count = 0
for i in st:
    if i in 'aeiou':
        count = count + 1
print(count)
'''