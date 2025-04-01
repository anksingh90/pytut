class Employe:
    def __init__(self,name,age,sal):
        self._name = name #protected
        self.__age = age #private
        self.sal = sal # public
    
    def get_age(self):
        return self._name
    
    def p_emp(self):
        print(f"Name : {self._name}, with salary of : {self.sal} and age : {self.__age}.")

emp = Employe("Amit", 30, 60000)

#print(emp.sal)
#print(emp.name)
print(emp.p_emp())