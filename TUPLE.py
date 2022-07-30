# tuple1=()
# print(type(tuple1))

# tuple1 = (1,2,3,1.1,2.2,3.3,'Python')
# print(tuple1)
# print(tuple1[0])
# tuple1[0]=200
# print(tuple1)


# str1="hi"
# str1[0]="vv"
# print(str1)

# li=[1,2,3,4]
# li[0]=200
# print(li)

# tuple2=1,2,3,4
# print(tuple2)
#
# tuple3=1,2,3,4
# print(tuple3)

# tu=()
# print(type(tu))

# tu=(55)
# print(type(tu))

# tu=(55,)
# print(type(tu))

# tu = (["Python",1,2.2],)
# print(type(tu))

# tuple1=(1,2,3,4,5,6,7,8,9,10)
# print(tuple1)
# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[5])
# print(tuple1[-1])

# tuple1=(1,)
# print(tuple1[-1])
# print(tuple1[0])

#tuple1 = (1,2,3,4,5,6,7,8,9,10)
# print(tuple1[0:5])
# print(tuple1[5:])
# print(tuple1[-1:-5])
# print(tuple1[-1:-5:-1])
# print(tuple1[-5:])
# print(tuple1[::2])
# print(tuple1[1::2])
#print(tuple1[::-1])

##delete tuple
# tuple1 = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
# #print(tuple1[0])
# #del tuple1[0]
# del tuple1
# print(tuple1)

##Tuple operation
# student_name="Abhi","Rohit","Krishna"
# class_name="7th","8th","10th"
# print(student_name+class_name)
# print(class_name+student_name)
# print(student_name*2)
# print(class_name*2)



# print("Sourav" + " " + "SInha")

# student_names = "Abhi","Rohit","Krishna"
# class_names = "7th","8th","10th"
# combine_tuple = student_names + class_names
# print(student_names,type(student_names))
# print(class_names,type(class_names))
# print(combine_tuple,type(combine_tuple))

##Acces items using from loop
#student_name="Abhi","Rohit","krishna"
# for name in student_name:
#     print(name)
#
# for index in range(len(student_name)):
#     print(student_name[index])
#
# for index,name in enumerate(student_name):
#     print(index,name)


##membership operator
# student_names = "Abhi","Rohit","Krishna"
# print("Abhi" in student_names)
# print("Akshith" in student_names)

# student_names = "Abhi","Rohit","Krishna"
# print("Abhi" not in student_names)
# print("Akshith" not in student_names)

# student_name="Abhi","Rohit","krishna"
# if ("Abhi" in student_name):
#     print("student in present in tuple")
# else:
#     print("student not present in tuple")
#
# student_name="Abhi","Rohit","krishna"
# if ("Rohan" in student_name):
#     print("student in present in tuple")
# else:
#     print("student not present in tuple")

# student_names="Abhi","Rohit","krishna"
# if ("Abhi" not in student_names):
#     print(f"Student is not present in the tuple")
# else:
#     print(f"Student is present in the tuple")

#student_names="Abhi","Rohit","krishna","Abhi"
#print(student_names.count("Abhi"))
#print(student_names.index("Abhi",1))

##copy

# tuple1=(1,2,3,4)
# tup_list=list(tuple1)
# tup_list[0]=1000
# tuple2=tuple(tup_list)
# print(tuple2)
# print(tuple1)
# #
# tuple1=(1,2,3,4)
# li1=list(tuple1)
# #print(li1)
# li1.append(5)
# #print(li1)
# tuple2=tuple(li1)
# print(tuple2)
# print(tuple1)

##DEEPCOPY
import copy

# tuple1=(1,2,3,4)
# li=list(tuple1)
# li[1]=1000
# tuple2=tuple(copy.deepcopy(li))
# print(tuple2)
# print(tuple1)

# tuple1 = (4,5,[6,7],8)
# tuple2 = copy.deepcopy(tuple1)
# tuple2[2][1] = 6000
# print(tuple1)
# print(tuple2)

# tuple1=(1,2,3,4,5)
# print(tuple1)
# print(sum(tuple1))
# print(max(tuple1))
# print(min(tuple1))





