# str1="Python and Data Science"
# # print(str1.upper())
# print(str1.lower())
# print(str1.title())
# print(str1.capitalize())
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.strip())
# print(str1.swapcase())
# print(str1.isalpha())
# print(str1.isalnum())
# print(str1.isdigit())
# print(str1.islower())
# print(str1.isupper())
# print(str1.istitle())
# print(str1.replace("Python","Machine"))
# print(str1.index("and"))
# print(str1.find("or"))
# print(str1.split())
# print(str1.zfill(30))
# print(str1.center(25))
# print(str1.startswith("P"))
# print(str1.endswith("e"))
# print(str1.count("a"))

# str1= "machine learning"
# last_index=str1.find("g")
# print(last_index+1)


# str1="This is orange juice"
# if("orange" in str1):
#     print(f"orange is present")
# else:
#     print(f"orange is not  present")


# a="0123456789sss"
# if(a.isdigit()):
#     print(f"is_digit")
# else:
#     print(f"is not digit")



# li1=[10,154,17,18]
# def swaplist(li):
#     n=li[0],li[-1]
#     return n
# print(swaplist(li1))


# list=[]
# num=int(input("Enter how many number"))
# for i in range(1,num+1):
#     list.append(int(input()))
# print(list)
# length=len(list)
# list[0],list[length-1]=list[length-1],list[0]
# print(list)

# li1=[1,2,3,4,5]
# mul=1
# for i in li1:
#     mul=mul*i
# print(mul)

# input_list=[2,5,6,12]
# # output_list=[]
# # for i in input_list:
# #     output_list.append(i**2)
# # print(output_list)
#
# output_list=[i**2 for i in input_list]
# print(output_list)
# even_no=[i for i in range(1,151) if (i%2==0)]
# print(even_no)
# odd_no=[i for i in range(1,151) if(i%2!=0)]
# print(odd_no)

# li1=[10,20,30,40,50]
# li1.remove(max(li1))
# print(max(li1))
# print(li1)

# li1=[1,2,3,4,5]
# li2=[]
# for i in li1:
#     li2.append(i)
# print(li2)

# li1=[1,2,3,4,5]
# li2=[6,7,8,9,10]
# li1.extend(li2)
# print(li1)

#li1=[5,3,3,1,5]
# li1.insert(2,33)
# print(li1)
#li1.remove(2)
#li1.pop()
#li1.clear()
# del li1
# print(li1)
# li1.sort()
# li1.reverse()
# print(li1.count(3))
# print(li1)
# print(sorted(li1))
# print(sum(li1))
# print(reversed(li1))

# li1=(1,2,3,3,3,4,5)
# print(li1)
# print(li1.index(3))
# print(li1.count(3))


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
#     if c[0]=="code":
#         count+=1
#     if c[1]=="Mcq":
#         count+=10
# print(count)

# class a:
#     def dispaly(self):
#         print("Class A method")
# class b:
#     def dispaly(self):
#         print("class B method")
# class c(a,b):
#     pass
# d=c()
# d.dispaly()
# from abc import as ABC, abstractmethod
# class abstract(ABC):
#     @abstractmethod
#     def do_somthing(self):
#         print("Some implemetation")


##MRO-Method Resolvation order -in mro define order in which base clases are searched when method exicution.first search in with the classs if not found follow the order tis order is callad linearizaion of the class and set a rules this is called as Mro
# class A:
#     def rk(self):
#         print("In class A")
# class B:
#     def rk(self):
#         print("In class B")
# class C(A,B):
#     def __init__(self):
#         print("Constructor C")
# r=C()
# print(C.__mro__)

# from abc import ABC ,abstractmethod
# class father(ABC):
#     @abstractmethod
#     def disp(self):
#         pass
#     def show(self):
#         print("Concrete method")
#
# class child(father):
#     def disp(self):
#         print("Chiled class")
#         print("Abstract class method")
# c=child()
# c.disp()
# c.show()

# from contextlib import contextmanager
# @contextmanager
# def enter_exist(text):
#     print("Entering")
#     yield text
#     print("Existing")
#
# with enter_exist("Attempt1")as t:
#     print(t)


# from contextlib import contextmanager
# @contextmanager
# def my_open(file,mode):
#     f=open(file,mode)
#     yield f
#     f.close()
#
# with my_open("Sample_with.txt","w") as f:
#     f.write("Hallo i am using python\n")
#
# with my_open("Sample_with.txt","a") as f:
#     f.write("Hallo i am using python2")
#
# import os
# print(os.getcwd())


# class greek:
#     def __init__(self,age=0):
#         self.__age=age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,x):
#         self.__age=x
# obj=greek()
# obj.set_age(21)
# print(obj.get_age())
# print(obj.set_age)

# def decorator_func(func):
#     def wraper_func():
#         print("wraper function worked")
#         return func()
#     print("decorator_func worked")
#     return wraper_func()
# @decorator_func
# def show():
#     print("show worked")
# print(show)

# decorator_show=decorator_func(show)
# print(decorator_show)

# ls=[i for i in range (10) if i%2]
# print(ls)


# for i in range (10):
#     if(i%2):
#         print(i)

# d1={n:n*n for n in range(1,10)}
# print(d1)

# def sqr(n):
#     for i in range (1,n+1):
#         yield i*i
# a=sqr(3)
# print(next(a))
# print(next(a))
# print(next(a))

# iter_list=iter(["A","B","C"])
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))

# n=int(input("Enter the nymber-"))
# print(f"The no is before reverse={n}")
# reverse=0
# while(n>0):
#     reverse=reverse*10+n%10
#     n=n//10
#
# print(f"The no is after reverse={reverse}")

# class person():
#     def __init__(self,name):
#         self.name=name
#         print(f"Name is={self.name}")
#     def say_hi(self):
#         print("Hello my name is:-",self.name)
# p=person("Rahul")
# # p.say_hi()





def decor(num):
    def inner_func():
        print("Inner function")
        a=num()
        add=a+5
        return add
    return inner_func

@decor
def num():
    return 10









