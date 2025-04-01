class Student:
    def __init__(self,name,student_id):
        self.s_name = name
        self.s_id = student_id
        self.l_course = []

    def enroll(self,course):
        self.course = course
        if self.course not in self.l_course:
            self.l_course.append(self.course)
            return f"cousre added: {self.l_course}"
        else : 
            return " Course already exists"
        
    def drop(self,dr_op):
        self.c_drop = dr_op
        if self.c_drop in self.l_course:
            self.l_course.remove(self.c_drop)
            return f"course removed: {self.l_course}"
        else:
            return "no such course enrolled"
        
    def list_courses(self):
        if self.l_course:
            return f"list of courses student enrolled in :{self.l_course} "
        else:
            return "no course enrolled"

s1 = Student("Dia",233244)
print(s1.enroll("maths"))
print(s1.list_courses())
print(s1.drop("maths"))
print(s1.list_courses())
print(s1.drop("chem"))
