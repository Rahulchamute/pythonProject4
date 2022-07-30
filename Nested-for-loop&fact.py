## for loop
# str1="Machine Learning"
# # for char in str1:
#     print(char)
#
# for index in range(len(str1)):
#     print(str1[index])

#li=[1,2,3,4]
# for val in li:
#     print(val)

# for inex in range (len(li)):
#     print(li[inex])

##for else

# for i in range(5):
#     print(f"The value of i={i}")
# print("iteration over")

# for i in range(5):
#     print(f"The value of i={i}")
# else:
#     print("iteration over")

# for i in range(5):
#     print(f"The value of i={i}")
#     if(i==3):
#         break
# else:
#     print("iteration over")
#
# for i in range(5):
#     print(f"The value of i={i}")
#     if(i==3):
#         continue
# else:
#     print("iteration over")

##factorial

# n=int(input("Enter the number="))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print(fact)
#
# n=int(input("Enter the number="))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

## nested for loop
# for i in range(5):
#     print(f"i={i}")
#     for j in range(3):
#         print("python")
# cnt=0
# for i in range(5):
#     print(f"i={i}")
#     for j in range(5):
#         print("python")
#         cnt+=1
#     print(cnt)

# for var1 in range(3):
#     print(var1)
#     for var2 in [1,2]:
#         print(var2)
#         for var3 in "Hi":
#             print(var3)
#         print()

# for i in range(3):
#     for j in range(2):
#         print("*****")
#     print()

# for i in range(3):
#     print(i)
#     for j in range(3):
#         print("*")
#     print()

# for i in range(3):
#     print(i)
#     for j in range(3):
#         print("*",end=" ")
#     print()
#
# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("A",end="")
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         print("1",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         print(i+1,end=" ")
#     print()
#
#
# for i in range(5):
#     for j in range(5):
#         print(j+1,end=" ")
#     print()
#



# n=5
# for i in range(1,5):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=6
# for i in range(1,n):
#     for s in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# for i in range(5,0,-1):
#     for s in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

n=6
for i in range(0,n+1):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
