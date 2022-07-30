##lambda function

# x=lambda a,b,c : a+b+c
# print(x(5,6,7))
#print((lambda a,b : a*b)(5,6))

##print((lambda a,b,c : (a+b+c)/3)(5,6,7))

# x=lambda a,b,c : (a+b+c)/3
# print(x(5,6,7))

# x=lambda *args : sum(args)
# print(x(1,2,3,4,5))
#
# x=lambda *args : max(args)
# print(x(1,2,3,4,5))

# x=lambda **kwargs : sum(kwargs.values())
# print(x(a=5,b=6,c=8))

# li1 = [1,2,3,4,5]
# li2 = [5,6,7,8,9]
# li3 = [1,2,3,4]
#
# square_lambda = lambda li : [i ** 2 for i in li]
#
# print(square_lambda(li1))
# print(square_lambda(li2))
# print(square_lambda(li3))

# x = lambda a,b : print(f"{a} is smaller than {b}") if a < b else print(f"{a} is greater than {b}")
# print(x(5,6))
# print(x(9,6))

##Built of fuction
##zip function
# names=["Ajit","Saurbh","Sahil","sakhi","Gaurav"]
# marks=[78,67,88,98,90]
# print(zip(names,marks))
# print(list(zip(names,marks)))
# print(tuple(zip(names,marks)))
# print(dict(zip(names,marks)))

##filter()

# li_iterable = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(even_check, li_iterable)))


