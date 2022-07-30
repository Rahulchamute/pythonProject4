# def outer_fun():
#     print("This is outer function")
#     def inner_fun():
#         print("This is inner function")
#     return inner_fun
#
# outer_fun()

# def outer_fun():
#     print("This is outer function")
#     def inner_fun():
#         print("This is inner function")
#     return inner_fun()
#
# obj1=outer_fun()
# print(obj1)

def dec1(fun):
    def nowexec():
        print("Exisicute now")
        fun()
        print("Exicuted")
    return nowexec
@dec1
def who_is_harry():
    print("Harry is good boy")

who_is_harry()