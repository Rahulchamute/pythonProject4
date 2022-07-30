
# class cal1():
#     def add(self,a,b):
#         res=a+b
#         print(res)
#
# obj1=cal1()
# obj1.add(5,6)

# class cal1():
#     x=5
#     y=6
#     str1="demo"
#     def __init__(self,a,b):
#         print("This is __init__ method")
#         self.a=a
#         self.b=b
#         print(f"value of a={self.a}")
#         print(f"value of b={self.b}")
#
#     def addition(self):
#         self.add=self.a+self.b
#         var2=100
#         print(f"Addition is={self.add}")
#         print(f"value of x={self.x}")
#         print(f"value of x={self.y}")
#
# obj1=cal1(7,6)
# obj1.addition()


# class className():
#     x=5
#     y=6
#
#     def method1(self):
#         print("This is method 1")
#         var=100
#         self.city="pune"
#         self.state="Maharastra"
#     def method2(self):
#         print("This is method 2")
#         self.method1()
#         print(f"city name={self.city}")
#         print(f"city name={self.state}")
#         print(f"value of x={self.x}")
#         print(f"value of y={self.y}")
#
# obj1=className()
# #obj1.method1()
# obj1.method2()

##single inheritance

# class companyinfo():
#     def __init__(self,company_name,companay_location):
#         print(f"This is company __init__ method")
#         self.company_name=company_name
#         self.company_location=companay_location
#
#     def get_company_name(self):
#         print("company_name=",self.company_name)
#     def get_company_location(self):
#         print("company_location=",self.company_location)
#
# class employeeinfo(companyinfo):
#     def __init__(self,company_name,companay_location,emp_name,salary):
#         print("This is employye __init__ method")
#         companyinfo.__init__(self,company_name,companay_location)
#         self.emp_name=emp_name
#         self.salary=salary
#     def get_emp_name(self):
#         print("employee_name=",self.emp_name)
#
#     def get_salary(self):
#         print("salary",self.salary)
#
# obj1=employeeinfo("TCS","pune","kishor",6000)
# obj1.get_company_name()
# obj1.get_salary()


# class companyinfo():
#     def __init__(self,company_name,companay_location):
#         print(f"This is company __init__ method")
#         self.company_name=company_name
#         self.company_location=companay_location
#
#     def get_company_name(self):
#         print("company_name=",self.company_name)
#     def get_company_location(self):
#         print("company_location=",self.company_location)
#
# class employeeinfo1(companyinfo):
#     def __init__(self,company_name,companay_location,emp_name,salary):
#         print("This is employye __init__ method")
#         companyinfo.__init__(self,company_name,companay_location)
#         self.emp_name=emp_name
#         self.salary=salary
#     def get_emp_name(self):
#         print("employee_name=",self.emp_name)
#
#     def get_salary(self):
#         print("salary",self.salary)
#
# class employeeinfo2(companyinfo):
#     def __init__(self,company_name,companay_location,emp_name,salary):
#         print("This is employye __init__ method")
#         companyinfo.__init__(self,company_name,companay_location)
#         self.emp_name=emp_name
#         self.salary=salary
#     def get_emp_name(self):
#         print("employee_name=",self.emp_name)
#
#     def get_salary(self):
#         print("salary",self.salary)
#
# obj1=employeeinfo1("TCS","pune","kishor",6000)
# obj1.get_company_name()
# obj1.get_salary()
# obj2=employeeinfo2("INFO","mumbai","rohit",8000)
# obj2.get_emp_name()


## list
# li1=[1,2,3,4,5,6,7,8,9]
# print(li1[0])

# city_name=["Pune","Mumbai","Kolkata","Newasa"]
# city=input("Enter the city name=")
# if (city in city_name):
#     print("city name present city_name")
# else:
#     print("city not present in city_name")

# li1=[]
# n=int(input("How many element of list"))
# for i in range(n):
#     b=int(input("Enter element of list"))
#     li1.append(b)
# print(li1)

# li1=[1,2,3]
# li2=[4,5,6]
# li1.extend(li2)
# print(li1)

# li1=[1,2,3,4,5]
# li1.insert(2,55)
# print(li1)

#li1=[1,2,3,4,5]
# li1.remove(3)
# print(li1)
# li1.pop()
# print(li1)
# li1.clear()
# print(li1)

# li1=[4,5,3,8,4,8,1]
# # li1.sort()
# # print(li1)
# # #print(sorted(li1))
# # li1.reverse()
# # print(li1)
# print(reversed(li1))

# li=[1,2,3,4,5]
# sq_li=[i**2 for i in li]
# print(sq_li)

# li1=[1,2,3,4,5]
# li2=li1
# print(li2)
# li2[2]=200
# print(li1)

# li1=[1,2,3]
# li2=li1.copy()
# print(li2)
# li2[2]=200
# print(li1)
# print(li2)

# li1=[1,[4,5],2,3]
# li2=li1.copy()
# print(li2)
# li2[1][1]=8
# print(li1)
# print(li2)

# import copy
# li1=[1,2,[3,4],5]
# li2=copy.deepcopy(li1)
# print(li2)
# li2[2][1]=200
# print(li1)
# print(li2)

# import time
# start_time=time.time()
# print(start_time)

#import datetime
# current_datetime=datetime.datetime.today()
# print(current_datetime)
# current_datetime=datetime.datetime.today().date()
# print(current_datetime)

# current_datetime=datetime.datetime.today().date()
# print(current_datetime)
# for i in range(-10,10):
#
#     new_date=current_datetime+datetime.timedelta(i)
#     print(new_date)


# current_datetime=datetime.datetime.today()
# print(current_datetime)
# print(current_datetime.strftime("%Y"))
# print(current_datetime.strftime("%y"))
# print(current_datetime.strftime("%d"))
# print(current_datetime.strftime("%a"))
# print(current_datetime.strftime("%A"))
# print(current_datetime.strftime("%m"))
# print(current_datetime.strftime("%u"))
# print(current_datetime.strftime("%U"))
# print(current_datetime.strftime("%b"))
# print(current_datetime.strftime("%B"))

# d1="05-07-2022"
# date_format="%d-%m-%Y"
# new_date=datetime.datetime.strptime(d1,date_format)
# print(new_date)

# s1={1,2,3,4,5}
# # print(s1)
# # s1.add(6)
# # print(s1)

# import pandas as pd
# pd.Dataframe(np.ones((5,5),int))
# check1=["Learn","Quiz","practice","Contribute"]
# check2=check1
# print(check2)
# check3=check1
# print(check3)
# check2[0]="code"
# print(check2)
# print(check1)
# print(check3)
# # check3[1]="Mcq"
# # print(check1)
# # print(check3)
# # print(check2)
# count=0
# for c in (check1,check2,check3):
#     if c[0]=="code":
#         count+=1
#     if c[1]=="Mcq":
#         count+=10
# print(count)

# check1=["Learn","Quiz","practice","Contribute"]
# check2=check1
# print(check2)
# check3=check1[:]
# print(check3)
# check2[0]="code"
# print(check2)
# print(check1)
# print(check3)
# check3[1]="Mcq"
# print(check1)
# print(check3)
# print(check2)
# count=0
# for c in (check1,check2,check3):
# #    if c[0]=="code":
# #        count+=1
#     if c[1]=="Mcq":
#         count+=1
# print(count)

# def addToList(listcontainer):
#     listcontainer +=[10]
#     print(listcontainer)
#
# mylistContainer=[10,20,30,40]
# addToList(mylistContainer)
# print(len(mylistContainer))

# namelist=["Harsh","Pratik","Bob","Dhru"]
# print(namelist[1][-1])

# a=True
# b=False
# c=False
# # if not a or b:
#     print(1)
# elif not a or not b and c:
#     print(2)
# elif not a or b or not b and a:
#     print(3)
# else:
#     print(4)

# if a or b and c:
#     print("Hello")
# else:
#     print("hello")

# count=1
# def doThis():
#     global count
#     for i in (1,2,3):
#         count +=1
# doThis()
# print(count)

import os
print(os.getcwd())
# f=open("sample.txt","w")
# f.write("HI i am laearning python")
# f.close()

# data = """Machine learning (ML) is the study of computer algorithms that can improve automatically
# through experience and by the use of data.[1] It is seen as a part of artificial intelligence.
# Machine learning algorithms build a model based on sample data, known as training data, in order
# to make predictions or decisions without being explicitly programmed to do so."""
# f=open("Machine Larning.txt","w")
# f.write(data)
# f.close()

# f=open("sample.txt","r")
# print(f.read())
# f.close()

# file = open("new_file.txt","w")
# file.write("This is first line\n")
# file.write("This is second line\n")
# file.write("This is third line\n")
# file.write("This is forth line\n")
# file.write("This is fifth line\n")
# file.write("This is sixth line\n")
# file.close()
#
# file=open("new_file.txt")
# d1=file.readline()
# file.close()
# print(d1)

# txt = """Machine learning algorithms are used in a wide variety of applications, such as in
# medicine, email filtering, speech recognition, and computer vision, where it is difficult or
# unfeasible to develop conventional algorithms to perform the needed tasks."""
# with open("Sample_with.txt","w") as file:
#     file.write(txt)
# with open("Sample_with.txt","r") as file:
#     print(file.read())


# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def type(self):
#         print("India is a developing country.")
#
#
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def language(self):
#         print("English is the primary language of USA.")
#
#     def type(self):
#         print("USA is a developed country.")
#
# obj_india=India()
# obj_usa=USA()
# for country in (obj_india,obj_usa):
#     country.capital()
#     country.language()
#     country.type()
# import sys
# list1=[1,2]
# print(list1)
# print(sys.getrefcount(list1))
# list2=list1
# print(sys.getrefcount(list2))
# del list2
# print(sys.getrefcount(list1))