# def decor(num):
#     def inner_fun():
#         a=num()
#         add=a+5
#         print(f"addition is={add}")
#         return add
#     return inner_fun
#
# def num():
#     return 10
#
# num=decor(num)
# num()

def sq_li(li):
    for i in li:
        sqr=i**2
        print(f"square of {i}={sqr}")
        yield sqr
obj=sq_li([1,2,3,4,5])
print(obj)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
