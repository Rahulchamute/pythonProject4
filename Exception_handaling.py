## index error
# li=[0]
# print(li[1])

##Atribute error
# tu=()
# print(tu.append(10))

##indentation error
# for i in range(10):
#     print(i)

##zero division error
#print(50/0)

##file not found error
# f=open("New.txt","r")
# print(f.read())
# f.close()

###try and except error

# try:
#     print("we are try bolck")
# except:
#     print("we are except block")


# try:
#     print("we are try bolck")
#     print(a)
# except:
#     print("we are except block")

# try:
#     print(a)
#     print("we are try bolck")
# except:
#     print("we are except block")

# try:
#     tuple1=(1,2,3,4,5)
#     print(tuple1[10])
#     print("we are try block")
# except:
#     print("we are except block")
# import os
# print(os.getcwd())


# with open("New.txt","w") as file1:
#     file1.write("We are learning python")
#
# try:
#     with open ("New.txt","x") as file1:
#         file1.write("New_msg")
# except:
#     with open ("New.txt","a") as file1:
#         file1.write(" and Machine Learning")
# with open("New.txt") as file1:
#     print(file1.read())
import traceback

# try:
#     a=5
#     b=0
#     print(a/b)
# except:
#     print("expect block")
#     print(traceback.print_exc())


# try:
#     a=5
#     b=0
#     print(a/b)
# except ZeroDivisionError as error:
#     print(error)

# text = """Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data.[1] It is seen as a part of artificial intelligence."""
# try:
#     f=open("ML.txt","x")
#     f.write(text)
#     f.close()
# except:
#     print(traceback.print_exc())
#     print("except block")
#
# text = """Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data.[1] It is seen as a part of artificial intelligence."""
# try:
#     f=open("ML.txt","x")
#     f.write(text)
#     f.close()
# except:
#     print(traceback.print_exc())
#     print("except block")
#
#
# text = """Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data.[1] It is seen as a part of artificial intelligence."""
# try:
#     f=open("ML.txt","x")
#     f.write(text)
#     f.close()
# except FileExistsError as error:
#     print(error)


##try-except-else
# try:
#     print("we are in try block")
# except:
#     print("we are except block")
# else:
#     print("we are else block")

# try:
#     print(a)
#     print("we are in try block")
# except:
#     print("we are except block")
# else:
#     print("we are else block")
#
# try:
#     print("we are in try block")
#     print(a)
# except:
#     print("we are except block")
# else:
#     print("we are else block")

# try:
#     print("we are in try block")
# except:
#     print("we are except block")
# else:
#     print("we are else block")
# finally:
#     print("we are finally block")
#

# try:
#     print("we are in try block")
#     string="ram"+123
# except:
#     print("we are except block")
# else:
#     print("we are else block")
# finally:
#     print("we are finally block")

# try:
#     string="ram"+123
#     print("we are in try block")
# except:
#     print("we are except block")
# else:
#     print("we are else block")
# finally:
#     print("we are finally block")


# try:
#     print("In the try block")
#     string = "ABC" + 123
# except:
#     print(traceback.print_exc())
#     print("In the except block")
# else:
#     print("In the else block")

# try:
#     try:
#         try:
#             print("we are try block")
#         except:
#             print("we are 3rd except block")
#     except:
#         print("we are 2nd except block")
# except:
#     print("we are 1st except block")


# try:
#     try:
#         try:
#             print("we are try block")
#             a+b
#         except:
#             print("we are 3rd except block")
#     except:
#         print("we are 2nd except block")
# except:
#     print("we are 1st except block")


try:
    try:
        try:
            print("we are try block")
        except:
            print("we are 3rd except block")
    except:
        print("we are 2nd except block")
    print(a+b)
except:
    print("we are 1st except block")



