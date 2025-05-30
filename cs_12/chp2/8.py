# List in python with sub functions

lst=[1,2,3,4,5]
for i in lst:
    print(i)
a=lst[::2]
b=lst[1:6]
c=lst[::-1]
print(a)
print(b)
print(c)
lst.append(10)
print(lst)
del lst[2:4]
print(lst)
print(lst.index(10))
lst.insert(2,45)
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst[3]=333
print(lst)