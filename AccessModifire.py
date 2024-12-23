# Public

class A():
    def __init__(self):
        self.a = 1
    def show(self):
        return f"The Public Number Is {self.a}"
    
public1 = A()
print(public1.show()) 


# Protected
class Student():
    def __init__(self, name,grade):
        self._name = name
        self._grade = grade
    
    def display_info(self):
        return f"Name: {self._name}, Grade: {self._grade}"
    
class ScholarshipStudent(Student):
    def __init__(self, name, grade, scholarship):
        self._scholarship = scholarship
        super().__init__(name, grade)
        
    def _info(self):
        return f"Name: {self._name}, Grade: {self._grade}, Scholarship:{self._scholarship}"
    
    def display_info(self):
        return self._info()
    
s1 = Student( "Mina" , 4)
print(s1.display_info())

ss1 = ScholarshipStudent("Rina" , 4 , 900)
print(ss1.display_info())


# Private 
class Employee():
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def __display_salary(self):
        return f"Name: {self.__name}, Salary: {self.__salary}"
    
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    
    def get_display_salary_method(self):
        return self.__display_salary()
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        self.__department = department 
        super().__init__(name, salary)
        
    def display_salary(self):
        return f"{self.get_display_salary_method()} Department:{self.__department}"
    
M1 = Manager("Mina" , 19000 , "CSE")
print(M1.display_salary())