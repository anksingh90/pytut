# dictionary {key : value}

''''={1:"cs" , 2:"phy" , 3:"chem"}
for i in dict:
    print (dict[i])
    print(dict)
dict[1]="maths"
print(dict)
dict["4"]="cs"
print(dict)

dict = {}
for i in range(3):
    key = input('Enter your class : ')
    val =input("Enter your Name : ")
    dict[key]= val

print(dict)'''


stu = {'10': 'Amit', '12': 'Ami', '11': 'AA'}
print(stu.keys())
print(stu.values())