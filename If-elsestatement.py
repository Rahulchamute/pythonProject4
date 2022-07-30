###24-03-2022

##if-else

# str1="jupyter notebook"
# # print(str1.islower())
# if(str1.islower()):
#     print("String is in lower case")
# else:
#     print("string is not lower case")

# str1="Jupyter notebook"
# # print(str1.islower())
# if(str1.islower()):
#     print("String is in lower case")
# else:
#     print("string is not lower case")
#
# str1="JUPETER NOTEBOOK"
# # print(str1.islower())
# if(str1.isupper()):
#     print("String is in UPPER case")
# else:
#     print("string is not UPPER case")

# str1="jupyter notebook"
# if(str1.isalnum()):
#     print("string is Alphanumeric")
# else:
#     print("string is not Alphanumeric")
#
# tr1="jupyternotebook"
# if(str1.isalnum()):
#     print("string is Alphanumeric")
# else:
#     print("string is not Alphanumeric")

# str1="jupyter notebook"
# if(str1.isalpha()):
#     print("string is Alphanumeric")
# else:
#     print("string is not Alphanumeric")
#
# str1="jupyternotebook"
# if(str1.isalpha()):
#     print("string is Alphanumeric")
# else:
#     print("string is not Alphanumeric")

# str1="python"
# if(str1):
#     print("string is not empty")
# else:
#     print("string is empty")

# str1=""
# if(str1):
#     print("string is not empty")
# else:
#     print("string is empty")

# a=40
# b=40
# if(a>b):
#     print("a is greater than b")
# elif(a==b):
#     print("a is equal to b")
# else:
#     print("b is greater than a")
#
# a=50
# b=40
# if(a>b):
#     print("a is greater than b")
# elif(a==b):
#     print("a is equal to b")
# else:
#     print("b is greater than a")
#
# a=50
# b=60
# if(a>b):
#     print("a is greater than b")
# elif(a==b):
#     print("a is equal to b")
# else:
#     print("b is greater than a")

# a=100
# b=100
# if(a>=b):
#     print("a is equal to b")
# else:
#     print("a is not equal to b")

# a=30
# b=20
# c=10
# if(a>b and a>c):
#     print("a is greater than b&c")
# else:
#     print("a is not greater than b&c")

# a=10
# b=50
# c=20
# if(a>b and a>c):
#     print("a is greater than a&b")
# elif(b>a and b>c):
#     print("b is greater than a&c")
# else:
#     print("c is greater than b&c")

# a=10
# b=50
# c=20
# if(a>b or a>c):
#     print("a is greater than a&b")
# elif(b>a or b>c):
#     print("b is greater than a&c")
# else:
#     print("c is greater than b&c")

# a=int(input("Enter the value of a:-"))
# b=int(input("Enter the value of b:-"))
# c=int(input("Enter the value of c:-"))
# print(f"a=={a},b=={b},c=={c}")

# a=20
# b=10
# c=5
# if((a>b and a>c) or a==20):
#     print("a is greater than b&c")
# elif((b>a and b>c) or b==50):
#     print("b is greater than a&c")
# else:
#     print("c is greater than b&c")

# a=20
# b=50
# c=5
# if((a>b and a>c) or a==20):
#     print("a is greater than b&c")
# elif((b>a and b>c) or b==50):
#     print("b is greater than a&c")
# else:
#     print("c is greater than b&c")

# a=20
# b=50
# c=100
# if((a>b and a>c) or a==20):
#     print("a is greater than b&c")
# elif((b>a and b>c) or b==50):
#     print("b is greater than a&c")
# else:
#     print("c is greater than b&a")

## pass statement

# str1="shubham"
# str2="naik"
# if(str1==str2):
#     print("string are same")
# else:
#     pass

# str1="shubham"
# str2="shubham"
# if(str1==str2):
#     print("string are same")
# else:
#     pass

# str1 = "Shubham"
# str2 = "Naik"
# if (str1 == str2):
#     pass
#     print(f"string 1 >> {str1}")
#     print(f"string 2 >> {str2}")
#     print("Both are equal strings")
# else:
#     print("Strings are different")
#     pass

# str1 = "Shubham"
# str2 = "Shubham"
# if (str1 == str2):
#     pass
#     print(f"string 1 >> {str1}")
#     print(f"string 2 >> {str2}")
#     print("Both are equal strings")
# else:
#     pass

# str1 = "Shubham"
# for i in str1:
#     if(i=="h"):
#         pass
#     else:
#         print(i)

# str1 = "Shubham"
# for i in str1:
#     if(i=="h"):
#         print(i)
#     else:
#         pass

## Nested if-else

# x=200
# if(x>100):
#     print("x is greater than 100")
#     if(x>150):
#         print("x is greater than 150")
#     else:
#         print("x is less than 150")
# else:
#     print("x is less than 100")

# x=140
# if(x>100):
#     print("x is greater than 100")
#     if(x>150):
#         print("x is greater than 150")
#     else:
#         print("x is less than 150")
# else:
#     print("x is less than 100")


# x=80
# if(x>100):
#     print("x is greater than 100")
#     if(x>150):
#         print("x is greater than 150")
#     else:
#         print("x is less than 150")
# else:
#     print("x is less than 100")

# cibil_score=800
# age=40
# salary=20000
# if(cibil_score>750):
#     print("cibil score is greater than 750")
#     if(age>25 and age<60):
#         print("age is between 25 to 60")
#         if(salary>40000):
#             print("Salary is greater than 40000\nLoan Approved")
#         else:
#             print("Loan Declined due to less income")
#     else:
#         print("Loan Declined due age criteria")
# else:
#     print("Loan Declined due to cibil_score")


# cibil_score=800
# age=40
# salary=50000
# if(cibil_score>750):
#     print("cibil score is greater than 750")
#     if(age>25 and age<60):
#         print("age is between 25 to 60")
#         if(salary>40000):
#             print("Salary is greater than 40000\nLoan Approved")
#         else:
#             print("Loan Declined due to less income")
#     else:
#         print("Loan Declined due age criteria")
# else:
#     print("Loan Declined due to cibil_score")

# cibil_score=760
# age=65
# salary=20000
# if(cibil_score>750):
#     print("cibil score is greater than 750")
#     if(age>25 and age<60):
#         print("age is between 25 to 60")
#         if(salary>40000):
#             print("Salary is greater than 40000\nLoan Approved")
#         else:
#             print("Loan Declined due to less income")
#     else:
#         print("Loan Declined due age criteria")
# else:
#     print("Loan Declined due to cibil_score")

## short hand if else
# a = 50
# b = 60
# if a > b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# a=50
# b=60
# print("a is greater than b") if (a>b) else print("b is greater than a")
# 

