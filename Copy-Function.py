##1.Equal to operator
# li1=[1,2,3,4,5]
# li2=li1
# print(li2)
# li2[2]=200
# print(li1,li2)

# li1=[[1,2,3],4,5]
# li2=li1
# print(li2)
# li2[0][1]=200
# print(li1,li2)

# li1=[[1,2,3],[4,5,6]]
# li2=li1
# print(li2)
# li2[1].append(100)
# print(li1,li2)

##2.shallow copy
# li1=[1,2,3]
# li2=li1.copy()
# print(li2)
# li2[0]=100
# print(li1,li2)

# li1=[[1,2,3],4,5]
# li2=li1.copy()
# print(li2)
# li2[0][1]=200
# print(li1,li2)

# li1 = [[1,2,3],4,5]
# li2 = li1.copy()
# print("Before Modification")
# print(f"List1 :- {li1}")
# print(f"List2 :- {li2}")
# li2[1] = 2000
# print("After Modification")
# print(f"List1 :- {li1}")
# print(f"List2 :- {li2}")


##deep copy
import copy
# li1=[1,2,3,4,5]
# li2=copy.deepcopy(li1)
# print(li2)
# li2[0]=1000
# print(li1,li2)

# li1=[1,3,4,5,[11,22,33]]
# li2=copy.deepcopy(li1)
# print(li2)
# li2[4][0]=1100
# print(li1,li2)
#
# li1=[1,3,4,5,[11,22,33]]
# li2=copy.deepcopy(li1)
# print(li2)
# li2[4].append(1100)
# print(li1,li2)
