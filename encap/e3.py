# Class Student, init = roll_no, name, list of marks. Method - init , display, avg_marks

class Student:
    def __init__(self,roll_no,name,l_marks):
        self.roll_no = roll_no
        self.name = name
        self.l_marks = l_marks

    def display(self):
        print("Roll No. :",self.roll_no)
        print("Name:",self.name)
        print("list of marks:", self.l_marks)

    def avg_mrks(self):
        sum = 0
        for i in self.l_marks:
            sum = i + sum
        print(sum/4)
        print('Total Marks : ',sum)


l_marks = [50,60,70,80]
s1 = Student("aaa",10,l_marks)
#s1.display()
s1.avg_mrks()