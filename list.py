##List
# 1.List is a collection of items
# 2.It allows data types like :- int, float, list, string, tuple, set, dict...
# 3.Used to store sequence of various data types

##Properties
# Orderd Data Type
# Mutable >> We can change the values
# Duplicates are allowed
# Lists are defined by square brackets >> [ ]
# Items are comma separated.

# li=[1,2,3,4,5,5,4]
# print(li,type(li),len(li))

li = ["data", 22, 44, [1,2,3], 5.5]
print(li)
#
# print(li[0])
# print(li[1])
# print(li[2])
# print(li[-1])

# str1 = "Akshay"
# str1[0] = 'a'
# # print(str1)
# li = ["data", 22, 44, [1,2,3], 5.5]
# print(li)
# li[0]="DATA"
# print(li)


##indxing
# li=[1,2,3,4,5]
# print(li)
# print(li[0],li[1],li[-1],li[3],li[-2])

##slicing
# li = [5,3,7,6,8,3.3,4.5,1.2,2.1,"Rishi","Anupam","Vicky"]
# print(li)
# print(li[0:2],li[:2],li[3:],li[1:8])
# print(li[::])
# print(li[::-1])
# print(li[-5:-1])
# print(li[-1:-5:-1])

## chek in list
# li = [5,3,7,6,8,3.3,4.5,1.2,2.1,"Rishi","Anupam","Vicky"]
# print(7 in li)
#
# li = [5,3,7,6,8,3.3,4.5,1.2,2.1,"Rishi","Anupam","Vicky"]
# print(77 in li)

# li = [5,3,7,6,8,3.3,4.5,1.2,2.1,"Rishi","Anupam","Vicky"]
# print(7 not in li)
#
# li = [5,3,7,6,8,3.3,4.5,1.2,2.1,"Rishi","Anupam","Vicky"]
# print(77 not in li)

# city_name=["mumbai","pune","delhi","chennai"]
# city="mumbai"
# if(city in city_name):
#     print(f"{city} in the list")
# else:
#     print(f"{city} not in list")

#city_name=["Pune","Mumbai","Delhi","Chennai"]
# for city in city_name:
#     print(f"welcome to {city}")

# city_name=["Pune","Mumbai","Delhi","Chennai"]
# for index,city1 in enumerate(city_name):
#     print(index,f"welocome to {city1}")

##range

# print(range(1,5))
# print(type(range(1,5)))
#print(list(range(1,5)))
# print(list(range(1,11)))
# print(list(range(5)))
# print(list(range(1,16,2)))
# print(list(range(0,16,2)))


# for i in range(5):
#     print(i,end=" ")

li = [5,3,7,6,8,3.3,4.5,1.2,2.1,"Rishi","Anupam","Vicky"]
#for i in range(len(li)):
#     print(li[i])
# for i in range(len(li)):
#     print(i)
# for i in range(len(li)):
#     print(i,li[i])
# for i in range(0,len(li),2):
#     print(i,li[i])

# for i in li:
#     if(type(i)==str):
#         print(i.upper())

# for i in li:
#     if(type(i)==str):
#         print(i.upper())
#     elif(type(i)==int):
#         print(i+10)
#     else:
#         print(i)










