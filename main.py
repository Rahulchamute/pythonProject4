# a,b=1,2
# print(a,b)

# str1="Python"
# print(str1[0])
# print(str1[1])
# print(len(str1))
# print(str1[0:6:1])
# print(str1[0:6:2])
# print(str1[0:3])
# print(str1[:5])
# print(str1[::1])
# print(str1[::2])
# # #print(str1[0:5:-1]) # not possible o/p
# print(str1[5:0:-1])
# print(str1[::-1])
# print(str1[1::2])
# print(str1[::2])
# str1="madam"
# print(str1[::-1])

##21-03-2022

str1="pyhon & data science"
# print(str1[-1:])
# print(str1[-1:-5:-1])
# print(str1[-5:-1])
# print(str1[-1:-10:-1])

##if -else in using string

# if('data science'in "Python & data science"):
#     print("substring is present")
# else:
#     print("substring is not present")


# if('data science'in "Python & data Science"):
#     print("substring is present")
# else:
#     print("substring is not present")

# var=False
# if(var):
#     print("somthing")
# else:
#     print("somthing else")

# var=True
# if(var):
#     print("somthing")
# else:
#     print("somthing else")

# age=int(input("enter your age:-"))
# if(age>=18):
#     print("Eligible for voting")
# else:
#     print("not eligible")

## string function
#1.Upper function

# str1="Python & Data Science"
# print(str1.upper())
#
# str1="Python & Data Science"
# if(str1.upper()=="PYTHON & DATA SCIENCE"):
#     print("yes")

##2.lower
# str1="Python & Data Science"
# print(str1.lower())

##3.title

# str1="python & data science"
# print(str1.title())

##4.Caplitalize
# str1="python & Data Science"
# print(str1.capitalize())

## lstrip()
# str1="   python & Data Science   "
# print(str1.lstrip())

## rstrip()
# str1="   python & Data Science   "
# print(str1.rstrip())

## strip()
# str1="   python &   Data Science   "
# print(str1.strip())

## swapcase()

# str1="Python & Data Science"
# print(str1.swapcase())

## replace()

# str1="Python & Data Science"
# print(str1.replace("Python","java"))

# str1="Python,Python,Python  & Data Science"
# print(str1.replace("Python","java",-1))
#
# str1="Python,Python,Python  & Data Science"
# print(str1.replace("Python","java",2))

## string operator

# str1="python "
# print(str1*2)
#
# str1="python "
# print(str1*4)
#
# str1="python "
# print(str1+str1)

##22-03-2022
## index()

# str1="Python & Data Science"
# print(str1.index("&"))
#
# str1="Python & Data Science"
# print(str1.index("a"))
#
# str1="Python & Data Science"
# print(str1.index("a",10))
# #
# str1="Python & Data Science"
# print(str1.index("a",11))
#
# str1="Python & Data Science"
# print(str1.index("a",11,15))
#
# string = """Data science is an interdisciplinary field that uses scientific methods,
# processes, algorithms and systems to extract knowledge and insights from noisy, structured
# and unstructured data, and apply knowledge and actionable insights from data across a
# broad range of application domains,science """
# print(string.index("science"))
#
# string = """Data science is an interdisciplinary field that uses scientific methods,
# processes, algorithms and systems to extract knowledge and insights from noisy, structured
# and unstructured data, and apply knowledge and actionable insights from data across a
# broad range of application domains,science """
# string.index("and!",96,150)
#
# #find()
# str1="Python & Data Science"
# print(str1.find("Science"))
#
# str1="Python & Data Science"
# print(str1.find("Science's"))
#
# str1="Python & Data Science"
# print(str1.find("Science"))

# str1="Python & Data Science"
# if(str1.find("Pawan")!=-1):
#     print("substring is present")
# else:
#     print("substring not present")

# str1="Python & Data Science"
# if(str1.find("data")==-1):
#     print("substring is present")
# else:
#     print("substring not present")

# string = """Data science is an interdisciplinary field that uses scientific methods,
# processes, algorithms and systems to extract knowledge and insights from noisy, structured
# and unstructured data, and apply knowledge and actionable insights from data across a
# broad range of application domains,science """
# print(string.find("and",100,200))

##split()

# string = """Data science is an interdisciplinary field that uses scientific methods."""
# print(string.split())

# string = """Data science is an interdisciplinary field that uses scientific methods."""
# print(string.split("is"))

# string = """Data science is an interdisciplinary field that uses scientific methods."""
# print(len(string.split("field")))

# string = """ data science is an interdisciplinary field that uses scientific methods,
# processes, algorithms and systems to extract knowledge and insights from noisy, structured
# and unstructured data, and apply knowledge and actionable insights from data across a
# broad range of application domains,science """
# print(string.split("\n"))

# string = """ data science is an interdisciplinary field that uses scientific methods,
# processes, algorithms and systems to extract knowledge and insights from noisy, structured
# and unstructured data, and apply knowledge and actionable insights from data across a
# broad range of application domains,science """
# print(len(string.split("\n")))

## join()
# li=["class1","class2"]
# print("&".join(li))
# #
# # li=["class1","class2"]
# # print("*".join(li))

##startwith

# str1 = "Python & Data Science"
# print(str1.startswith("P"))
#
# str1 = "Python & Data Science"
# print(str1.startswith("y"))

# str1 = "DS/String/Indexing"
# str2 = "DS/String/Slicing"
# str3 = "DS/String/Functions"
# str4 = "ML/LR/GD"
# path_li = [str1,str2,str3,str4]
# print(path_li)
# for folder_name in path_li:
#     if (folder_name.startswith("DS")):
#         print(f"Folder = {folder_name}")
#     else:
#         print(f"Not Folder = {folder_name}")

##endswith():
# str1 = "Python & Data Science"
# res = str1.endswith("e")
# if (res) :
#     print("Yes")
# else:
#     print("No")

# str1 = "DS/String/Indexing.iypnb"
# str2 = "DS/String/Slicing.iypnb"
# str3 = "DS/String/Functions.iypnb"
# str4 = "ML/LR/GD.txt"
# path_li = [str1,str2,str3,str4]
# print(path_li)
# file_cnt = 0
# nfile_cnt = 0
# for file_name in path_li:
#     if file_name.endswith("iypnb"):
#         file_cnt += 1
#     else:
#         nfile_cnt += 1
# print(f"Total no of files = {file_cnt}\nTotal no of nfiles = {nfile_cnt}")


##isdigit() #only  0-9 digit allowed

# str1 = "123"
# print(str1.isdigit())

# str1 = "123sd"
# print(str1.isdigit())

##isalnum() #space not allowed only a-z and 0-9 digit allowed

# str1 = "123ABC"
# print(str1.isalnum())

# str1 = "123 ABC"
# print(str1.isalnum())

##isalpha  #only a-z  allowed

# str1 = "Python"
# print(str1.isalpha())
#
# str1 = "PYTHON & DS"
# print(str1.isalpha())

##isdecimal()  ###only  0-9 digit allowed ,dot and space not allowed
# str1 = "123"
# print(str1.isdecimal())

# str1 = "1.3"
# print(str1.isdecimal())

##islower() ## true return string contain only char with lower case

# str1 = "python"
# print(str1.islower())
#
# str1 = "Python"
# print(str1.islower())

##isupper() ##true return string contain only char with upper  case

# str1 = "PYTHON"
# print(str1.isupper())

# str1 = "PYTHON 123rd BATCH"
# print(str1.isupper())

##istitle()
# str1 = "Python And Data Science"
# print(str1.istitle())

# str1 = "Python ANd Data Science"
# print(str1.istitle())

##isspace()
# str1 = "   "
# print(str1.isspace())
#
# str1 = ""
# print(str1.isspace())

## zfill() # used for zero filling at starting

# str1 = "Python"
# print(str1.zfill(10))
#
# str1 = "Python"
# print(str1.zfill(7))

##center() ## it will added spaces on both side
# str1 = "Python"
# print(str1.center(7))
#
# str1 = "Python"
# print(str1.center(8))

# str1="harshal ramesh bangale"
# # A="harshal ramesh bangale"
# A=str1.replace("harshal","bangale",1).replace("ramesh","bangale",1).replace("bangale","ramesh",1))
# print(A)
