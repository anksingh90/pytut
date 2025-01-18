# sort 3 values using conditional statement

a = 3
b = 5
c = 7
if a>b and a>c:
    large = a
    if b>c:
        s_large = b
        s = c
    else :
        s_large = c
        s = b
elif b>a and b>c:
    large = b
else :
    large = c