'''
Lst = [1,2,3,4,5,6,7,8,9,10]
lst1 = [2,4,6,8,10]
lst2=[1,3,5,7,9]
'''
lst=[1,2,3,4,5,6,7,8,9,10]
lst_odd=[]
lst_even=[]

for i in lst:
    if i%2==0:
      lst_even.append(i)
    else:
       lst_odd.append(i)
print(lst_even)
print(lst_odd)
