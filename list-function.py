# li = []
# print(type(li))

#li=[1,2.2,3,"data",[1,2,3]]
# print(li)
# print(type(li))
# print(id(li))

# li=[1,2.2,3,"data",[1,2,3]]
# for i in li:
#     print(i)

##1.append()

# var=[]
# var.append(100)
# print(var)
# var.append(200)
# print(var)

# Value = []
# print(f"List before adding any item :- {Value}")

# Value.append("Data")
# print(Value)
#


# Value.append("Science")
# print(Value)
#
# Value.append("&")
# print(Value)
#
# Value.append("Machine Learning")
# print(Value)
# for i in Value:
#     print(i)

# li=[1,2,3]
# li.append("Python")
# print(li)

# li=[]
# li.append([1,2,3])
# li.append([4,5,6])
# print(li,len(li))
# for i in li:
#     print(i)

##extend

# li1=[1,2,3]
# li2=[4,5,6]
# li1.extend(li2)
# print(li1)
# for i in li1:
#     print(i)
# li2.extend(li1)
# print(li2)

# cities1 = ["Pune","Mumbai"]
# cities2 = ["Chennai","Delhi"]
# cities1.extend(cities2)
# for i in cities1:
#     print(i)
# len(cities1)

# li = [1,2,3,[1,2,3],[11,22,33]]
# # li[3].append(55)
# for i in li:
#     if type(i) == list:
#         i.append(4)
# print(li)

## insert()

# li=[1,2,3,4]
# li.insert(2,55)
# print(li)

# list1 = [1,2,3,4]
# list1.insert(0,55)
# print(list1)
# list1[0]=list1[0]-50
# print(list1)

# even_numbers=[]
# odd_numbers=[]
# for i in range(1,21):
#     if(i%2==0):
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
# print(f"Even_numbers:-{even_numbers}\nOdd_numbers:-{odd_numbers}")

# even_numbers = []
# odd_numbers = []
#
# li = [11, 21, 33, 22, 24, 34, 55, 65, 66, 76]
# for i in li:
#     #     print(i)
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
#
# print(f"Even Number list :- {even_numbers},\nOdd number list :- {odd_numbers}")

even_numbers = []
odd_numbers = []
float_numbers = []

# li = [11, 21, 3.3, 22, 24, 3.4, 55, 65, 66, 76, 4.5]
# for i in li:
#     #     print(i)
#     if type(i) == float:
#         float_numbers.append(i)
#     elif i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
#
# print(f"Even Number list :- {even_numbers},\nOdd number list :- {odd_numbers}\nFloat number list :- {float_numbers}")


# list1=[1,2,3,4]
# sq_li=[]
# for i in list1:
#     sq_li.append(i**3)
# print(sq_li)


## delete
##remove

# li=[1,2,3,4]
# li.remove(3)
# print(li)
#
# sub_names = ["Phy","Che","Math","Bio","Eng"]
# sub_names.remove("Bio")
# print(sub_names)

# sub_names = ["Phy","Che","Math","Bio","Eng"]
# value = "Bio"

# if value in sub_names:
#     sub_names.remove(value)
#     print("Item deleted")
# else:
#     print("Item is not present in the list")
# print(sub_names)

# sub_names = ["Phy","Che","Math","Bio","Eng"]
# sub_names.pop()
# print(sub_names)
#
# sub_names = ["Phy","Che","Math","Bio","Eng"]
# sub_names.pop(2)
# print(sub_names)

# sub_names = ["Phy","Che","Math","Bio","Eng"]
# cnt = 0
# for i in sub_names:
#     cnt += 1
# print(cnt)

##clear

# sub_names = ["Phy","Che","Math","Bio","Eng"]
# sub_names.clear()
# sub_names

##del_keyword

# sub_names = ["Phy","Che","Math","Bio","Eng"]
# print(sub_names)
# del sub_names
# print(sub_names)


##assending order

# numbers = [10,4,20,5,1,23,67,6]
# numbers.sort()
# print(numbers)

# li=[12,20,30,5.5,6.7,98,44,56]
# li.sort()
# print(li)

##decending order
# numbers=[10,4,20,5,1,23,67,6]
# numbers.sort(reverse=True)
# print(numbers)


# numbers=[10,4,20,5,1,23,67,6]
# numbers.sort()
# print(numbers[::-1])

##Max

# list=[1,2,3,4,5]
# print(max(list))

##min
# list=[1,2,3,4,5]
# print(min(list))

##sum()
# li=[1,2,3,4,5]
# print(sum(li))

# li1=[1,2,3,4,5]
# summation=0
# for i in li1:
#     summation+=i
# print(summation)

# li1=[1,2,3,[1,2,33]]
# summation_num=0
# summation_inner_num=0
# for i in li1:
#     if(type(i)==list):
#         for j in i:
#             summation_inner_num +=j
#     else:
#         summation_num +=i
# print(summation_num,summation_inner_num)


# li=[1,2,3,4,5]
# max_num=0
# for i in li:
#     if(max_num<i):
#         max_num=i
# print(max_num)

# li=[11,2,3,4,1]
# min_num=li[0]
# for i in li:
#     if(min_num>i):
#         min_num=i
# print(min_num)

# nest_li = [[1,2,3],[4,5,6],[7,8,9]]
# print(nest_li)
#
# li = [[1,2,3],[4,5,6]]
# print(li)

# nest_li = [[1,2,3],[4,5,6],[7,8,9]]
# print(nest_li)
# for sub_list in nest_li:
#     print(sub_list)
# for sub_list in nest_li:
#     print(sum(sub_list))
# for sub_list in nest_li:
#     print(max(sub_list))
# for sub_list in nest_li:
#     print(min(sub_list))
# print(nest_li[1:])
# print(nest_li[1:2])
# print(nest_li[0][0])
# print(nest_li[2][2])


# nest_li = [[1,2,3],[4,5,6],[7,8,9,10,11,12],["Abhi","Rishi","CHetan"]]
# print(nest_li)

# str1 = "Data Science & Machine Learning"
# str1_li=(str1.split())
# print(str1_li)
# print(" ".join(str1_li))
# print("-".join(str1_li))
# print("-".join("data"))

# str1="Laptop"
# new_li=[]
# for char in str1:
#     new_li.append(char.upper())
# print(new_li)

# li=[[1,2,3],[4,5,6]]
# new_li=[]
# for sub_li in li:
#     for item in sub_li:
#         new_li.append(item)
# print(new_li)

# li = [[1,2,3,],[4,5,6]] # [1,2,3,4,5,6]
# new_li = []
# for sub_li in li:
#     for item in sub_li:
#         new_li.append(item)
# print(new_li)

# li = [[1,2,3],[4,5,6],7,8,9] # [1,2,3,4,5,6,7,8,9]
# new_li = []
# for sub_li in li:
#     if type(sub_li) == list:
#         for item in sub_li:
#             new_li.append(item)
#     else:
#         new_li.append(sub_li)
# print(new_li)


##List Comprenesion

# li=[1,2,3,4,5]
# # cube_li=[]
# for item in li:
#     cube_li.append(item**3)
# print(cube_li)

##OR

# cube_li=[item**3 for item in li]
# print(cube_li)
#
# sq_li=[item**2 for item in li]
# print(sq_li)

# list1 = [4,1,3,6,7,8,10,11,34,36,20,55,77,99,100]
# # odd_li = []
# # even_li = []
# # for item in list1:
#     if item % 2 == 0:
#         even_li.append(item)
#     else:
#         odd_li.append(item)
# print(even_li,odd_li)

# even_li=[item for item in list1 if item % 2 == 0 ]
# print(even_li)
# odd_li = [item for item in list1 if item % 2 != 0]
# print(odd_li)

# li1=[2,3,4,5,6,10]
# li2=[4,5,6,7,8,9]
# li3=[]
# for val in li1:
#     if val in li2:
#         li3.append(val)
# print(li3)
