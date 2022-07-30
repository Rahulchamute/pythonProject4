# class base():
#     print("In the parent class ")
# class derived(base):
#     print("In the child class")
#
# d1=derived()

##single_inheritance
# class Company_Info():
#     company_area="Chinchwad"
#     def __init__(self,company_name,location):
#         self.company_name=company_name
#         self.location=location
#     def get_company_name(self):
#         print("company_name=",self.company_name)
#     def get_company_location(self):
#         print("company_location=",self.location)
#
# class EmployeeInfo(Company_Info):
#     def __init__(self,emp_name,salary,company_name,location):
#         print("Employee Information __init__ method")
#         Company_Info.__init__(self,company_name,location)
#         self.emp_name=emp_name
#         self.salary=salary
#
#     def get_emp_name(self):
#         print("emp_name=",self.emp_name)
#     def get_emp_salary(self):
#         print("Employee salary=",self.salary)
#
# obj1=EmployeeInfo("Rahul",70000,"TCS","pune")
# obj1.get_emp_name()
# obj1.get_emp_salary()
# obj1.get_company_name()
# obj1.get_company_location()
# print(obj1.company_area)

###multilevel inheritance
# class Baseclass1():
#     def __init__(self):
#         print("Baaseclass1 __inhit__ method")
#     def Addition(self):
#         self.add=self.a + self.b
#         print(f"Addition of {self.a} and {self.b} is {self.add}")
# class Baseclass2(Baseclass1):
#     def __init__(self):
#         Baseclass1.__init__(self)
#         print("Baseclass 2 __init__ method")
#     def Multiplication(self):
#         mul=self.a*self.b
#         print(f"multiplication of {self.a} and {self.b} is {mul}")
# class Derivedclass(Baseclass2):
#     def __init__(self,a,b):
#         Baseclass2.__init__(self)
#         print("Derived class __inhit__ method")
#         self.a=a
#         self.b=b
#
#     def division(self):
#         print("Divison is",self.a/self.b)
#
# d1=Derivedclass(50,5)
# d1.Addition()
# d1.division()
# d1.Multiplication()


##Multiple inheritance
# class Baseclass1():
#     def __init__(self,a,b):
#         print("This is Base class1 __init__ method")
#         self.a=a
#         self.b=b
#
#     def addition(self):
#         print("Addition method")
#         add=self.a+self.b
#         print(f"Addition of {self.a} and {self.b} ={add}")
# class Baseclass2():
#     def __init__(self,a1,b1):
#         print("This is base class 2 __init__ method")
#         print(f"a1 value= {a1}")
#         print(f"b1 value= {b1}")
#
#     def multiplcation(self,a,b):
#         print("multiplication method")
#         mul=a*b
#         print(f"Multiplication of {a} and {b} ={mul}")
#
# class Derivedclass(Baseclass1,Baseclass2):
#     def __init__(self,a,b,a1,b1):
#         print("this is derived class _inhit__ metod")
#         Baseclass1.__init__(self,a,b)
#         Baseclass2.__init__(self,a1,b1)
#
#     def calc(self):
#         print("calculation method")

# obj1=Derivedclass(10,20,"rohit","rohan")
# obj1.addition()
# obj1.multiplcation(5,6)
# obj1.calc()

##HIRachikal
# class Parent:
#     pass
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
#
# c1 = Child1()
# c2 = Child2()


class Company_Info():
    company_area="Chinchwad"
    def __init__(self,company_name,location):
        self.company_name=company_name
        self.location=location
    def get_company_name(self):
        print("company_name=",self.company_name)
    def get_company_location(self):
        print("company_location=",self.location)

class EmployeeInfo1(Company_Info):
    def __init__(self,emp_name,salary,company_name,location):
        print("Employee Information __init__ method")
        Company_Info.__init__(self,company_name,location)
        self.emp_name=emp_name
        self.salary=salary

    def get_emp_name(self):
        print("emp_name=",self.emp_name)
    def get_emp_salary(self):
        print("Employee salary=",self.salary)

class EmployeeInfo2(Company_Info):
    def __init__(self,emp_name,salary,company_name,location):
        print("Employee Information2 __init__ method")
        Company_Info.__init__(self,company_name,location)
        self.emp_name=emp_name
        self.salary=salary

    def get_emp_name(self):
        print("emp_name=",self.emp_name)
    def get_emp_salary(self):
        print("Employee salary=",self.salary)

obj1=EmployeeInfo1("Rahul",70000,"TCS","pune")
obj1.get_emp_name()
obj1.get_emp_salary()
obj1.get_company_name()
obj1.get_company_location()
print(obj1.company_area)
obj2=EmployeeInfo2("Rohan",50000,"info","pune")
obj2.get_emp_name()
obj2.get_emp_salary()
obj2.get_company_name()
obj2.get_company_location()



