##class structure

# var1=500
# class classname():
#     x=1
#     y=10
#     z="demo class"
#     def method1(self):
#         print("This is method 1")
#         var2="Data Science"
#         self.cityname="pune"
#         self.state="Maharastra"
#     def method2(self):
#         print("This is method 2")
#         var3="Machine Learning"
#         self.method1()
#         print("self.city name",self.cityname)
#         print("self.state",self.state)
#         print("self.x",self.x)
#         print("self.y",self.y)
#         print("self.z",self.z)

# obj=classname()
# print(obj.method1())
# print(obj.method2())
# print(obj.cityname)
# print(obj.state)


##__init__

# class empdetails():
#     location="Pune"
#     def __init__(self):
#         print("This in inhit method")
#     def emp_name(self):
#         pass
#     def emp_name(self):
#         pass
#     def compay_name(self,company):
#         print("we are company name")
#         print("company name",company)
#     def designation(self):
#         pass
#
# obj=empdetails()
# obj1=empdetails()
# print(obj.location)
# print(obj.compay_name("TCS"))

# class empdetails():
#     location="Pune"
#     def __init__(self,emp_name,salary,company_name,designation):
#         print("we are inhit method")
#         print("emp_name",emp_name)
#         print("salary_name",salary)
#         print("company_name",company_name)
#         print("designation",designation)
#         self.emp_name=emp_name
#         self.emp_salary=salary
#         self.company_name=company_name
#     def emp_name(self):
#         print("emp_name",self.emp_name)
#         print("company_location",self.location)
#     def emp_salary(self):
#         print("salary",self.salary)
#     def company_name(self):
#         print("company_name",self.company_name)
#     def emp_designation(self):
#         pass
#
# obj=empdetails("rahul",90000,"tcs","developer")
# print(obj.emp_name)
# print(obj.emp_salary)
# print(obj.company_name)
# print(obj.location)

# class name():
#     def __init__(self,fname,lname):
#         print("init method")
#         print("fname",fname)
#         print("lname",lname)
#         self.fname=fname
#         self.lname=lname
#     def get_firstname(self,age):
#         print(f"my first_name is{self.fname} and age {age}")
#     def get_lastname(self,age):
#         print(f"my first_name is{self.lname} and age {age}")
#     def get_fullname(self):
#         print(f"my full name is{self.fname}.{self.lname}")
#     def get_mailid(self):
#         print(f"my_mail id is={self.fname+self.lname}3@gmail.com")
#
# name1=name("rahul","chamute")
# print(name1.get_firstname(28))
# print(name1.get_lastname(28))
# print(name1.get_fullname())
# print(name1.get_mailid())
