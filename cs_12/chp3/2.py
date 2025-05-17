
def digi(str):
    a_count=0
    d_count=0
    for i in str:
        if i.isalpha():
            a_count+=1
        elif i.isdigit():
            d_count+=1
    print(a_count)
    print(d_count)

# main program starts
str="India is my country and i am proud of 123 its rich and varied heritage 823492"
digi(str)
