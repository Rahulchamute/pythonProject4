# def palindrame(s):
#     temp=s[::-1]
#     if(s==temp):
#         print("it is palindrame")
#     else:
#         print("Not palindrome")
# s="nitin"
# palindrame(s)

# n=int(input("Enter the no :"))
# print(f"The number before revrse:{n}")
# reverse=0
# while(n>0):
#     reverse=reverse*10+n%10
#     n=n//10
# print(f"after the revese no:{reverse}")

# def fibonnaci(n):
#     a,b=0,1
#     print(a)
#     while(b<n):
#         print(b)
#         c=a+b
#         a=b
#         b=c
# fibonnaci(150)


import numpy as np
import pandas as pd
# a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(a)
# print(a.ndim)
# print(a.reshape(3,4))
# a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# print(a[2][2])

# a=np.array([1,2,3,4,5,6])
# # print(a.reshape(3,2))
# for val in np.nditer(a):
#     print(val)
# for ind,val in np.ndenumerate(a.reshape(3,2)):
#     print(ind,val)

# a=np.zeros(10).reshape(5,2)
# print(a)
# a=np.ones(10)
# print(a)
# a=np.arange(1,13).reshape(3,4)
# print(a)
# a=np.linspace(1,50).reshape(10,5)
# print(a)
# a=np.eye(5)
# print(a)
# a=np.identity(4)
# print(a)
# a=np.random.rand(5)
# print(a)
# a=np.random.rand(4,5)
# print(a)
# a=np.random.randint(1,5)
# print(a)
# a=np.random.randint(1,20,size=10)
# print(a)
# a=np.random.randint(1,50,size=(4,5))
# print(a)
# a=np.array(np.random.randint(1,50,size=5))
# print(np.sort(a))
# a=np.array([[4,8,5],[6,4,3]])
# print(a)
# print(np.sort(a))

# a=np.array([1,2,3])
# print(np.append(a,50))

# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[5,6],[7,8]])
# print(np.append(arr1,arr2,axis=0))

# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[5,6],[7,8]])
# arr3=arr1+arr2
# print(arr3)

# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[5,6],[7,8]])
# print(np.concatenate([arr1,arr2]))

# a=np.ceil([4.4,6.7,8.9])
# print(a)
#
# a=np.array([4.5,6.7,7.1])
# print(np.around(a))

# li = [1,2,3,1,2,3,1,2,3]
#
# arr=np.array(li)
# print(arr)
# print(np.where(arr==2))


#student_name = {"Name":"Rohit", "Roll_No":56, "Marks":89, "Passout_Batch":'2020'}
# print(student_name)
# print(student_name["Name"])
# print(student_name.get("Name"))
# print(student_name.keys())
# print(student_name.values())
# print(student_name.items())

# for i in student_name.keys():
#     print(i)

# stu_marks = {
#     "Saurabh" : 88,
#     "Anuj"    : 89,
#     "Sakshi"  : 50,
#     "Ankita"  : 90
#  }
# print(stu_marks)

# employee_database = {
#     "Employee_Name": "Prashant",
#     "Company_Name": "TCS",
#     "Salary": 60000,
#     "Designation": "Python Developer"
# }
#
# new_data = {
#     "Company_Location": "Mumbai",
#     "Age": 30,
#     "Emp_Id": "CRD5563"
#
# }
#
# print(employee_database)
# employee_database.update(new_data)
# print(employee_database)

# emp_db = {'Emp_Name': 'Suhas',
#      'Company_Name': 'IOSTIO',
#      'Age': 26,
#      'Salary': 80000,
#      'Emp_Id': 'ARD6652'
# }
# print(emp_db)
# emp_db.popitem()
# #emp_db.pop('Salary')
# print(emp_db)
# squ_dict = {}
#
# first_n_number = int(input("Enter the number :- "))
# for i in range(1,first_n_number+1):
#         squ_dict.update({i:i ** 2})
#         print(squ_dict)
#
# print(squ_dict)



import datetime
#curr_time=datetime.datetime.now()
# print(curr_time)
# curr_date_time = datetime.datetime.today()
# print(curr_date_time)

# curr_date=datetime.datetime.today().date()
# print(curr_date)

# new_date=curr_date+datetime.timedelta(days=1)
# print(new_date)

# for i in range(-10,10):
#     new_date = curr_date + datetime.timedelta(days=i)
#     print(new_date)

# curr_time=datetime.datetime.today()
# print(curr_time)
#
# print(curr_time.strftime("%Y"))
# print(curr_time.strftime("%y"))
# print(curr_time.strftime("%d"))

# any_day = datetime.datetime(1990,5,15)
# print(any_day.strftime("%Y-%B-%d"))

# d1 = "25-11-2020"
# date_format = "%d-%m-%Y"
# new_date1 = datetime.datetime.strptime(d1,date_format).date()
# print("New Date1 :-",new_date1)

# import time
# start_time=time.time()
# li=[1,2,3,4,5]
# for i in li:
#     print(i)
#     time.sleep(2)
# end_time=time.time()
# total_time=end_time-start_time
# print(total_time)

import pandas as pd
import numpy as np
# dict_class = {
#     "Student_Names" : ["Abhishek","Swapnil", "Rohit","Pooja", "Prajkta"],
#     "Student_Age" : [22,24,27,23,24]
# }
# #print(dict_class)
# df=pd.DataFrame(dict_class)
#print(df)
# arr=np.arange(1,11).reshape(5,2)
# df=pd.DataFrame(arr,columns=list(A,B),index=[C,D,E,F,G])
# print(df)

# dict_class = {
#     "Student_Names" : ["Abhishek","Swapnil", "Rohit","Pooja", "Prajkta"],
#     "Student_Age" : [22,24,27,23,24]
# }
# print(dict_class)
# df=pd.DataFrame(dict_class)
# #print(df)
# df["Student_Marks"]=[75,80,66,76,67]
# print(df)
# df["Roll_no"]=np.array([1,2,3,4,5])
# print(df)

# arr=np.random.randint(1,50,size=(5,5))
# print(arr)
# df=pd.DataFrame(arr)
# print(df)

# import os
# print(os.getcwd())

# df=pd.read_csv("Heart_Data.csv")
# #print(df)
# # print(df.info())
# # print(df.describe())
# #print(df.head())
# #print(df.shape)
# print(df.columns)
# # for i in df.columns:
# #     print(i)
# col_list=df.columns.tolist()
# print(col_list)

# import pandas as pd
# emp_df=pd.read_csv("Emp_Records.csv")
# #print(emp_df)
# #print(emp_df[["Emp ID","First Name","Salary"]])
# # print(emp_df)
# # print(emp_df[0:5])
#
# print(emp_df.iloc[2:5,1:5])
# print(emp_df.loc[2:5,"Emp ID"])

# class Employee:
#     def __init__(self,fname,lname,pay):
#         self.fname=fname
#         self.lname=lname
#         self.pay=pay
#         print(f"first name is={self.fname}")
#         print(f"last name is={self.lname}")
#         print(f"last name is={self.pay}")
#     def get_fullname(self):
#         return f"{self.fname} {self.lname}"
#     def get_fullpay(self):
#         print(f"fullpay={self.pay}")
#
# obj1=Employee("Rahul","Chamute",1000)
# print(obj1.get_fullname())
# print(obj1.get_fullpay())


# class CompanyInfo():
#     company_area="Chinchwad"
#     def __init__(self,company_name,location):
#         print("The __init__ method 1 executed")
#         self.company_name=company_name
#         self.location=location
#     def get_company_name(self):
#         print(f"Company_name={self.company_name}")
#     def get_location(self):
#         print(f"company_location={self.location}")
#     @classmethod
#     def show(cls):
#        cls.company_area
# class Employeeinfo(CompanyInfo):
#     def __init__(self,company_name,location,emp_name,salary):
#         print("This is __init__ method 2 executed")
#         CompanyInfo.__init__(self,company_name,location)
#         self.emp_name=emp_name
#         self.salary=salary
#     def get_emp_name(self):
#         print(f"Company emp name={self.emp_name}")
#     def get_emp_salary(self):
#         print(f"emp_salary={self.salary}")
# obj1=Employeeinfo("valiant","Pune","Rahul",70000)
# print(obj1.get_company_name())
# print(obj1.get_location())
# print(obj1.get_emp_name())
# print(obj1.get_emp_salary())
# print(CompanyInfo.company_area)



# var1 = 5000  # Global Variable
#
#
# class ClassName():  # Class Name
#     x = 1  # Class Variables
#     y = 5.5  # Class Variables
#     z = "Demo Class"  # Class Variables
#
#     def method1(self):  # Method 1
#         print("This is my method 1")
#         var2 = "Data Science"  # Local Variable
#         self.city_name = "Pune"  # Instance Variable 1
#         self.state = "Maharashtra"  # Instance Variable 2
#
#     def method2(self):  # Method 2
#         print("This is my method 2")
#         var3 = "Machine Learning"
#         self.method1()
#         print("self.city_name", self.city_name)
#         print("self.x", self.x)
#         print("self.z", self.z)

# import math
# class square():
#     def __init__(self,side):
#         self.side=side
#
#     def area(self):
#         area_sq=self.side**2
#         print(f"Area of square is={area_sq}")
#
# class rectangle():
#     def __init__(self,b,l):
#         self.b=b
#         self.l=l
#     def area(self):
#         area_rec=self.b*self.l
#         print(f"Area of Rectangle is={area_rec}")
#
#
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         area_circle = math.pi * self.radius ** 2
#         print(f"Area of a circle = {round(area_circle, 2)}")
#
# def exe_fun():
#     c1=Circle(5)
#     s1=square(6)
#     r1=rectangle(7,8)
#     for obj in [c1,s1,r1]:
#         print(obj.area())
# exe_fun()

# class my_class():
#     def sum(self,a=None,b=None,c=None):
#         if(a!=None and b!=None and c!=None):
#             s=a+b+c
#         elif(a!=None and b!=None):
#             s=a+b
#         else:
#             s=a
#         return s
# obj=my_class()
# print(obj.sum(7))


# def decorator_func()
#
#
# def show():
#     print("show worked")

# def decor(num):
#     def inner_func():
#         print("Inner function")
#         a=num()
#         add=a+5
#         return add
#     return inner_func
#
# @decor
# def num():
#     return 10

#import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
#import pandas as pd


# a=range(1,11)
# res=list(map(lambda a:a*a,a))
# print(res)

# a=range(1,11)
# res=list(filter(lambda a:a%2==0,a))
# print(res)

# a=(lambda n:n+2)
# print(a(2))

# def my_max(li):
#     max=li[0]
#     for i in li:
#         if (i>max):
#             max=i
#     return max
# li1=[10,20,30,40,50]
# print("Maximum element=",my_max(li1))

# li1=[10,30,70,50,60]
# #print(max(li1))
# li1.sort()
# print(li1[-1])

# f=open("Sample.txt","w")
# f.write("Welcome the file handling")
# f.close()
# f=open("Sample.txt","a")
# f.write("Hi helloe")
# f.close()
# f=open("Sample.txt","r")
# print(f.read())
# f.close()
# f=open("Sample.txt","r")
# print(f.readline())
# f.close()

# data1 = """Machine learning (ML) is the study of computer algorithms that can improve automatically
# through experience and by the use of data.[1] It is seen as a part of artificial intelligence.
# Machine learning algorithms build a model based on sample data, known as training data, in order
# to make predictions or decisions without being explicitly programmed to do so."""
# # f=open("Machine Learning.txt","w")
# f.write(data1)
# f.close()
# data2 = """Machine learning (ML) is the study of computer algorithms that can improve automatically
# through experience and by the use of data.[1] It is seen as a part of artificial intelligence."""
# f=open("Machine Learning.txt","a")
# f.write(data2)
# f.close()
# f=open("Machine Learning.txt","r")
# print(f.read())
# f.close()
# f=open("Machine Learning.txt","r")
# print(f.readline())
# print(f.readline())
# f.close()

# with open("Sample2.txt","w") as file2:
#     file2.write("hi how are you")

#data1 = """Machine learning (ML) is the study of computer algorithms that can improve automatically
# through experience and by the use of data.[1] It is seen as a part of artificial intelligence.
# Machine learning algorithms build a model based on sample data, known as training data, in order
# to make predictions or decisions without being explicitly programmed to do so."""
# with open ("Sample3.txt","w") as file3:
#     file3.write(data1)
# data2 = """Machine learning (ML) is the study of computer algorithms that can improve automatically
# through experience and by the use of data.[1] It is seen as a part of artificial intelligence."""
#
# with open ("Sample3.txt","a") as file3:
#     file3.write(data2)
# with open ("Sample3.txt","r") as file3:
#     print(file3.read())


import os

# old_file="Sample2.txt"
# new_file="Sample4.txt"
# os.rename("Sample2.txt","Sample4.txt")

#os.rename("Sample4.txt","Sample5.txt")
print(os.getcwd())

# os.rename(r"C:\Users\Admin\PycharmProjects\pythonProject4\Sample3.txt","Sample7.txt")

# os.remove("new_file.txt")
# os,remove(r"C:\Users\Admin\PycharmProjects\pythonProject4\sample.txt")

# print(os.path.exists("Sample5.txt"))
# print(os.path.exists("Sample9.txt"))

# if os.path.exists("XYZ.txt"):
#     os.remove("XYZ.txt")
# else:
#     print("file not exist")

# if os.path.exists("Sample5.txt"):
#     os.remove("Sample5.txt")
#     print("File exist")
# else:
#     with open ("Sample5.txt","w") as file4:
#         file4.write("The new file created")

# if os.path.exists("Sample5.txt"):
#     os.remove("Sample5.txt")
#     print("File exist")
# else:
#     with open ("Sample5.txt","w") as file4:
#         file4.write("The new file created")

# folder_path="Database"
# if os.path.exists(folder_path):
#     print(f"{folder_path} exist ")
#     with open(r"C:\Users\Admin\PycharmProjects\pythonProject4\Database\sample9.txt","w")as g:
#         g.write("hi hello")
# else:
#     os.mkdir(folder_path)

# print(os.getcwd())
# path=r"C:\Users\Admin\PycharmProjects\pythonProject4"
# print(os.listdir(path))

# try:
#     print("We are try block")
# except:
#     print("we are expect block")

# try:
#     print(a)
#     print("We are try block")
# except:
#     print("we are expect block")

# try:
#     print("We are try block")
#     print(a)
# except:
#     print("we are expect block")

# try:
#     tu=(1,2,3,4,5,6)
#     print(tu[10])
#     print("We are try block")
# except:
#     print("we are expect block")

# with open ("Sample10.txt","w") as file:
#     file.write("We are learning python")
#
# try:
#     f=open("Sample10.txt","r")
#     print(f.read())
#     f.close()
# except:
#     print("file not exist")
#
#
# try:
#     f=open("Sample11.txt","r")
#     print(f.read())
#     f.close()
# except:
#     print("file not exist")

# try:
#     print("Try block exist")
# except:
#     print("Expect block")
# else:
#     print("else block")
# finally:
#     print("Finally block")

# class A:
#     print("class A")
# class B:
#     print("class B")
# class C(A,B):
#     pass
# obj=C
# print(obj)


# def square(n):
#     for i in range(1,n+1):
#         yield i*i
# obj=square(5)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

# iter_list=iter([1,2,3,4,5])
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))

# from abc import ABC,abstractmethod
# class father(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     def show(self):
#         print("Concreate Method")
#
# class child(father):
#     def display(self):
#         print("This is child class")
# obj=child()
# print(obj.display())
# print(obj.show())

# from contextlib import contextmanager
# @contextmanager
# def my_open(file,mode):
#     f=open(file,mode)
#     yield f
#     f.close()
#
# with open ("Sample11.txt","w") as file1:
#     file1.write("How are you")
# with open ("Sample11.txt","r")   as file1:
#     print(file1.read())

# class greek:
#     def __init__(self,age=0):
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def set_age(self,x):
#         self.__age=x
# obj=greek(10)
# print(obj.get_age())
# obj.set_age(15)
# print(obj.get_age())


# def decorator_func(func):
#     def wrapper_fun():
#         print("wrapper function worked")
#         return func()
#     print("decorator functon worked")
#     return wrapper_fun()
# @decorator_func
# def show():
#     print("Show worked")


# def decor(num):
#     def inner_func():
#         print("This is inner function")
#         a=num()
#         add=a+15
#         return add
#     print("worked decor function")
#     return inner_func()
# @decor
# def num():
#     return 10


# ls=[i for i in range(1,11) if i%2==0]
# print(ls)
#
# di={n:n*n for n in range(1,10)}
# print(di)