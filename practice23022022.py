##swaping
# a=5
# b=10
# print(a,b)
# a,b=b,a
# print(a,b)

# a,b,c,d="ram","rom","hard","soft"
# print(a,b,c,d)
# a,b,c,d=d,b,a,c
# print(a,b,c,d)

##print function=print function is used print any statement

# a=5
# b=10
# # print(a)
# # print(b)
# # print(a,b)
# # print(b,a)
# print("The value of a=",a)
# print("The value of b=",b)
# print(f"The value of a={a}and the value of b={b}")

## int
# a=10
# print(type(a))
# print(id(a))

##float
# a=6.7
# print(type(a))
# print(id(a))

## complex

# a=5+6j
# print(type(a))
# print(id(a))

##type of casting-type of casting means conversion of  one data type to another data type
## int to float
# a=5
# print(type(a))
# print(float(a))

##float to int
# a=5.5
# print(type(a))
# print(int(a))

##int to complex
# a=5
# print(type(a))
# print(complex(a))

##float to complex
# a=5.5
# print(type(a))
# print(complex(a))

#str
# age=56
# print(str(age))
#
# print(str('ss'))
#
# print(str(25.5))

# print(str(3+5j))

##Taking input from usrer
# age=int(input("enter age="))
# print(age)

# a=int(input("Enter 1st number:-"))
# b=int(input("Enter 2nd number:-"))
# c=a+b
# print("addition of a and b is=",c)

# a=6
# b=float(a)
# print(b)

###String
# str1="python"
# print(str1[0])
# print(str1[1])
# print(str1[5])
# print(len(str1))
# print(str1[-1])

# str1="-----python-----"
# print(len(str1))
# cnt=0
# for i in str1:
#     cnt+=1
#     print(i)

# print(1,2,3,4,sep="\n")

## positive indexing
# str1="Python & Data Science"
# print(str1[0::])
# print(str1[0:8:])
# print(str1[0:8:1])
# print(str1[0::1])
# print(str1[0::2])
# print(str1[0:8:-1]) # -1 o/p is nothing
# print(str1[2:10:])

##Negative indexing
# str1="Python & Data Science"
# # print(str1[-1:-5:])# o/p not possible
# print(str1[-1:-5:-1])
# print(str1[-5:-1:])


# str1="madam"
# str2=str1[::-1]
# print(str2)
# if(str1==str2):
#     print("they are equal")
# else:
#     print("they are not equal")


# for i in range(0,20,2):
#     print(i,end=" ")

# li=[5,10,15,"kishor","snehal",4.5,6.5]
# print(li)
# for i in li:
#     print(i,end=" ")

# li=[5,10,15,"kishor","snehal",4.5,6.5]
# print(li)
# for i,j in enumerate (li):
#     print(i,j,end=" ")

# for i in range(0,16,4):
#     print(i)

# li=list(range(0,16))
# print(li)
# for i in range(0,len(li),4):
#     print(i)

# x=int(input("Enter the no"))
# if(x>0):
#     for i in range(2,x):
#         if(x%2==0):
#             print(" not prime no")
#             braek
#         else:
#             print("not prime no")
#             break
# else:
#     print("give positive no")

# a=1,2,3,4,5
# print(type(a))
# for c in a:
#     print(c)

# my_list=(10,20,30,40,50,60)
# it=iter(my_list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# str1="Python & Data science"
# str2="Data science"
# if('Data science' in "Python & Data science"):
#     print("string is valid")
# else:
#     print("string no valid")

# li=["Data","science",13,15,5.5,6.6]
# li1=["science"]
# if(li1 in li):


# str1=str(input("Enter the string Element:-"))
# vovel=["a","e","i","o","u"]
# for word in vovel:
#     if(word==vovel):
#         str1.lower()
#         str.replace()
#
# li=[[1,2,3,4],[5,6,7,8]]
# li1=[]
# for i in li:
#     li1.append(li[0][0])
#     li1.append(li[1][0])
# print(li1)


# li=[1,2,3,4,5]
# max_num=0
# for i in li:
#     if(max_num<i):
#         max_num=i
# print(max_num)

# li=[1,2,3,4,5]
# min_num=li[0]
# for i in li:
#     if(min_num>i):
#         max_num=i
# print(min_num)

# li=[[1,2,3,4],[5,6,7,8]]
# li1=[]
# for i in li:
#     for j in i:
#         li1.append([0][4])


# def TransposeMatrix(matrix):
#     for i in range(len(matrix)):
#         for j in range (len(matrix[0]))
#             result[j][i]=matrix[i][j]
#
# x=[[12,4],
#    ]
#


# string = "machine learning"
# last_letter = string[-1]
# print(string.index(last_letter) + 1)



# str1="0123456789"
# even_no=0
# odd_no=0
# for i in str1:
#     if(int(i)%2==0):
#         even_no+=1
#         print(f"Even_no:-{i}",end="\n")
#     else:
#         odd_no+=1
#         print(f"odd_no:-{i}",end="\n")
# print(f"Total Even no count is:-{even_no}")
#print(f"Total Odd no count is:-{odd_no}")



# str1="Python  MachineLearning"
# print(str1)
# print(str1.upper())
# print(str1.lower())
# print(str1.title())
# print(str1.islower())
# print(str1.isupper())
# print(str1.istitle())
#print(str1.swapcase())
#print(str1.count("a",12,30))
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.strip())
# print(str1.isdigit())
# print(str1.isalnum())
# print(str1.isalpha())
#print(str1.isdecimal())
#print(str1.replace("Machine Learning","Data Science"))
# print(str1.startswith("Python"))
# print(str1.endswith("Learning"))
# print(len(str1))
# last_character=str1[-1]
# print(str1.index(last_character)+1)
#print(str1.index("a",11))
#print(str1.find("a",11))
# print(str1.find("z"))
#print(str1.zfill(30))
#print(str1.center(30))
#print(str1.split())

# str1="Python  MachineLearning"
# print(str1)
# str2=str1.split()
# print(" & ".join(str2[::-1]))

# str1="Python & Machine Learning"
# print(str1)
# str2=str1.split()
# print(" ".join(str2[::-1]))

#li1=[1,2,3,4]
# li1.append(5)
# print(li1)
# li1.append([1,2])
# print(li1)

# li1=[1,2,3]
# li2=[4,5,6]
#li1.extend(li2)
#print(li1)
# li2.extend(li1)
# print(li2)

# li1=[1,2,3,4]
# li1.insert(2,55)
# print(li1)

# li1=[1,2,3,4]
# li1.remove(3)
# print(li1)

# li1=[1,2,3,4]
# li1.pop()
# print(li1)
#
# li1=[1,2,3,4]
# li1.pop(2)
# print(li1)

# li1=[1,2,3,4]
# li1.clear()
# print(li1)

# li1=[1,2,3,4]
# del.li1
# print(li1)


# number=[10,9,5,7,6,3,]
# number.sort()
# print(number)

# number=[10,9,5,7,6,3,]
# number.sort()
# print(number[::-1])

# li=[1,2,6,7,8,12]
# print(max(li))
#
# li=[1,2,6,7,8,12]
# print(min(li))
#
# li=[1,2,6,7,8,12]
# print(sum(li))

# li1=[1,2,3,4]
# li2=li1
# print(li2)
# li2[2]=200
# print(li2)
# print(li1)

# li1=[1,2,3,4,[1,2],5,6]
# li2=li1.copy()
# print(li2)

# li1=[1,2,3,4,[1,2],5,6]
# li2=li1.copy()
# print(li2)

# li1=[1,2,3,4,[1,2],5,6]
# li2=li1.copy()
# li2[4][0]=200
# print(li2)
# print(li1)
import copy

# li1=[1,2,3,4,[1,2],5,6]
# li2=copy.deepcopy(li1)
# print(li2)
# li2[4][1]=1000
# print(li2)
# print(li1)

# student_name="abhi","rohit","abhi","abhi"
# print(student_name.count("abhi"))
#
# student_name="abhi","rohit","abhi","abhi"
# print(student_name.index("abhi",1))

# str1="Rahul chamute"
# print(str1[::-1])

# str1="rahul
#        chamute"
# print(str1,end='')

# subject=["Phy","chem","math","Bio","Eng"]
# for i in subject:
#        print(i)

# subject=["Phy","chem","math","Bio","Eng"]
# for i in range(len(subject)+1):
#        print(i)

# subject=["Phy","chem","math","Bio","Eng"]
# for i in range(len(subject)):
#        print(subject[i])


# li1=[1,2,3,4,5,6]
# print(li1.index(3))

# li1=[1,2,3,4,4,4,5,6]
# print(li1.count(4))

# tu=(1,2,3,4,5)
# tu2=tu.index(5)
# print(tu2)

# tu=(1,2,2,2,3,4,5)
# tu2=tu.count(2)
# print(tu2)


li=[1,2,3,4,5]


def list_1(num):
    max1=max(num)
    min1=min(num)
    sum1=sum(num)
    return max1,min1,sum1



max1,min1,sum1=list_1([1,2,3,4,5,6,7])
print(max1,min1,sum1)








