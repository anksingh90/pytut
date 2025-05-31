'''
using randint() create number of students between 4 - 8, assign random values varies between 50 - 98.
Then assign grades between 
Grade A : 90 - 100
Grade B : 80 - 89
Grade C : 70 - 79
Grade D : 50 - 69
'''

import random
stu_len=random.randint(4,8)

for i in range(1,stu_len+1):
    stu_marks = random.randint(50,98)
    if stu_marks>=50 and stu_marks <= 69:
        print('Student : ',i,'Marks : ',stu_marks,'Grade : D')
    elif stu_marks>=70 and stu_marks <= 79:
        print('Student : ',i,'Marks : ',stu_marks,'Grade : C')
    elif stu_marks>=80 and stu_marks <= 89:
        print('Student : ',i,'Marks : ',stu_marks,'Grade : B')
    elif stu_marks>=90 and stu_marks <= 100:
        print('Student : ',i,'Marks : ',stu_marks,'Grade : A')
    