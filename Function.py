# def hello_function():
#     print("Hello function")
#
# hello_function()

# def my_fun():
#     print("_" * 35)
#     print("We are learning python functions")
#     print("We are defining user defined function")
#     print("_" * 35)
#
# my_fun()
# my_fun()
# my_fun()


# def split_string(string):
#     string1=string.lower()
#     print("lower string is",string)
#     li=string.split()
#     print("splited string is",li)
#
# str1=" Data & science "
# str2="Machine Learning"
# split_string(str1)
# split_string(str2)

# def max_func(li):
#     print(max(li))
#
# li1=[1,2,3,4,5]
# li2=[8,9,10,50,75]
# max_func(li1)
# max_func(li2)

# def print_statement(num):
#     print("We are in the print statement function")
#     for i in range(num):
#         print(f"{i}th iteration = We are learning Python Functions")
#
# print_statement(5)

# def Avg_func(a,b):
#     print(f"value of a={a},value of b={b}")
#     avg=(a+b)/2
#     print(avg)
#
# a=int(input("enter the value a:"))
# b=int(input("enter the value of b:"))
#
# Avg_func(a,b)

# def calculation(a,b):
#     add=a+b
#     mul=a*b
#     return add,mul
# a=int(input("Enter Value of a:"))
# b=int(input("Enter value of b:"))
# addition,multiplication=calculation(a,b)
# print(addition)
# print(multiplication)

# def calculation(a,b):
#     add = a + b
#     mul = a * b
#     div = a / b
#     return add,mul,div,"Succesfull"
#
# addition,multiplication,division,msg = calculation(20,30)
# print(addition,multiplication,division)
# print(msg)

# def calculation(li):
#     max1=max(li)
#     min1=min(li)
#     sum1=sum(li)
#     return max1,min1,sum1
#
# li1=[5,6,7,8,9,10]
# maximum,minimun,summation=calculation(li1)
# print(maximum)
# print(minimun)
# print(summation)

# def input_list(num):
#     li=[int(input("Enter element")) for i in range(num)]
#     a=(min(li))
#     b=(max(li))
#     c=(sum(li))
#     return (a,b,c)
# num=int(input("Enter number of elements"))
# min_list,max_list,sum_list=input_list(num)
#
# print(f"minimum value is {min_list},maximum is {max_list},sum of list is {sum_list}")

##Type of Argument
##Positinal argument

# def fun(a,b):
#     print(f"a={a},b={b}")
# fun(4,5)
#
# def fun(a,b):
#     print(f"a={a},b={b}")
# fun(4,[1,2,3])

# def fun(a,b):
#     print(f"a={a},b={b}")
# fun((1,2,3),4)

# def fun(a,b):
#     print(f"a={a},b={b}")
#     return a/b
# div=fun(8,4)
# print(div)

# def addition(num1,num2):
#     print(f"Num1={num1},Num2={num2}")
#     return num1+num2
#
# print(addition(4,5))
#
# def addition(num1,num2):
#     print(f"Num1={num1},Num2={num2}")
#     return num1+num2
#
# add=addition(4,5)
# print(add)

# def addition(x,y,z):
#     print(f"x={x},Y={y},Z={z}")
#     return x+y+z
# add=addition(10,20,30)
# print(add)

# def addition(x,y,z=100):
#     print(f"x={x},Y={y},Z={z}")
#     return x+y+z
# add=addition(10,20)
# print(add)

# def addition(x,y=200,z=100):
#     print(f"x={x},Y={y},Z={z}")
#     return x+y+z
# add=addition(10)
# print(add)

# def addition(x=100,y=100,z=100):
#     print(f"x={x},Y={y},Z={z}")
#     return x+y+z
# add=addition(y=10,z=20)
# print(add)

# def addition(x,y,z=100):
#     print(f"x={x},Y={y},Z={z}")
#     return x+y+z
# add=addition(10,20)
# print(add)

# def addition(x,y=100,z=100):
#     print(f"x={x},Y={y},Z={z}")
#     return x+y+z
# add=addition(10)
# print(add)

# def addition(x=100,y=100,z=100):
#     print(f"x={x},Y={y},Z={z}")
#     return x+y+z
# add=addition()
# print(add)

# def addition(x=100,y=100,z=100):
#     print(f"x={x},Y={y},Z={z}")
#     return x+y+z
# add=addition(z=300,x=50,y=150)
# print(add)

##Positional Argument
# def multiplication(a,b,c):
#     print(f"a={a},b={b},c={c}")
#     mul=a*b*c
#     return mul
# print(multiplication(5,6,7))

# def multiplication(a,b,c):
#     print(f"a={a},b={b},c={c}")
#     mul=a*b*c
#     return mul
# print(multiplication(5,b=6,c=7))


# def multiplication(*args):
#     print(f"argument={args}")
#
# print(multiplication(5,6,7))


# def multiplication(*variable):
#     print(f"Argument = {variable} & Its dtype = {type(variable)}")
#     mul = 1
#     for val in variable:
#         mul *= val
#
#     return mul
#
#
# print(multiplication(2, 3, 4, 5, 6))


# def test(**kwerge):
#     print(f"Kwergw={kwerge}")
#
# print(test(a=5,b=10,c=20,d=50))


# def summation(**kwargs):
#     print(f"Kwargs = {kwargs}, Dtype = {type(kwargs)}")
#     summation1=sum(Kwargs.values())
#     return summation1
#
# sum1=summation(a=10,b=20,c=30,d=40,e=50)
# print(sum1)


# def test(a, b, c, *args, x=10, y=20, **kwargs):
#     print(f"a={a},b={b},c={c}")
#     print(f"Args = {args}")
#     print(f"x={x},y={y}")
#     print(f"Kwargs = {kwargs}")
#
#
# test(11, 22, 33)


# def add(x,y):
#     print(x+y)
# def pass_argument(x,y):
#     add(x,y)
#
# x=5
# y=10
# pass_argument(x,y)

# def add(x,y):
#     print(x+y)
# def mul(x,y):
#     print(x*y)
# def div(x,y):
#     print(x/y)
#
#
# def pass_argument(x,y):
#     add(x,y)
#     mul(x,y)
#     div(x,y)
# x=10
# y=5
# pass_argument(x,y)


# def add(x,y):
#     print("Addition:-",x+y)
# def mul(x,y):
#     print("Multiplication:-",x*y)
# def div(x,y):
#     print("Division:-",x/y)
#
# def pass_argument(x,y):
#     operation=int(input("Enter \n1 for Addition \n2 for multiplication \n3 for Division"))
#     if(operation==1):
#         add(x,y)
#     elif(operation==2):
#         mul(x,y)
#     else:
#         div(x,y)
#
# x=10
# y=5
# pass_argument(x,y)

##Recursion

# num=5
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(f"factorial of {num} is {fact}")


# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     print(f"factorial of{num} is {fact}")
# factorial(5)

# def factorial(num):
#     if(num==1):
#         return 1
#     else:
#         return num * factorial(num-1)
# num=5
# print(f"factorial of {num} is {factorial(num)}")

# def fibo(n):  # 3
#     if n <= 1:  # Condition Failed
#         return n
#     else:
#         return fibo(n - 2) + fibo(n - 1)
#
#
# n = 10
# print("Fibonacci series = ", end=' ')
# for i in range(n):  # i = 3
#     print(fibo(i), end=' ')

