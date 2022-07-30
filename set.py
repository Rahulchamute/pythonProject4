# set1={}
# print(type(set1))

# set1=set{}
# print(type(set1))

# set1={1,2,3}
# print(type(set1))

# dict1={"a":12,"b":23}
# print(type(dict1))

# set1={1,2,2,3,4,5.5,6.6,7,8,9.69,9.69}
# print(set1)

# set1={1,2,2,3,4,5.5,6.6,7,8,9.69,9.69}
# print(len(set1),set1)

# set1={0,1,2,2,3,4,5.5,6.6,7,8,9.69,9.69,True,False}
# print(len(set1),set1)

# list1=[2,3,"a",5,1,"b",10,20,15,3.14,5.67,10,20,30]
# print(list1,len(list1))
# set1=set(list1)
# print(set1,len(set1))

# list1=[2,3,"a",5,1,"b",10,20,15,3.14,5.67,10,20,30]
# print(list1,len(list1))
# # set1=set(list1)
# # print(set1)
# # list1=list(set1)
# # print(list1)
# print(list(set(list1)))

# list1=[3,4,5,6,4,5,8,9]
# print(list(set(list1)))

# tu1=(3,4,5,6,4,5,8,9)
# print(tuple(set(tu1)))

# set1={1,2,3,[1,2,3]}


##aad function
# set1={3,4,5,6,7}
# set1.add(8)
# print(set1)

# set1={3,4,5,6,7}
# set1.add("data")
#print(set1)

##update Function
# set1={"phy","che","math"}
# set2={"bio","eng"}
# print(set1.update(set2))
#

# list1=[2,3,"a",5,1,"b",10,20,15,3.14,5.67,10,20,30]
# print(list1,len(list1))
# print(list(set(list1)))

# li1=[2,3,4,5,6,10]
# li2=[4,5,6,7,8,9]
# unique_item=[]
# for val in li1:
#     if val in li2:
#         unique_item.append(val)
# print(unique_item)
#
# li1=[2,3,4,5,6,10]
# li2=[4,5,6,7,8,9]
# unique_item=[]
# for val in li1:
#     if val not in li2:
#         unique_item.append(val)
# print(unique_item)


##add function
# set1={3,4,5,6,7}
# set1.add(8)
# print(set1)


##update
# sub_name1={"phy","che","math"}
# sub_name2={"bio","eng"}
# sub_name1.update(sub_name2)
# print(sub_name1)
# print(sub_name2)

# sub_name1={"phy","che","math"}
# sub_name2={"bio","eng"}
# sub_name2.update(sub_name1)
# print(sub_name1)
# print(sub_name2)

# li1={1,2,3,4,5}
# li2=[4,5,6,7]
# li1.update(li2)
# print(li1)
# print(li2)
#
# li1={1,2,3,4,5}
# li2=(4,5,6,7)
# li1.update(li2)
# print(li1)
# print(li2)

# li1={1,2,3,4,5}
# li2=(4,5,6,7)
# li3=li1.update(li2)
# print(li3)
# print(li2)

##Union
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# set3=set1.union(set2)
# print(set3)
#
# set1={1,2,3,4,5,6}
# set2=(4,5,6,7,8,9)
# set3=set1.union(set2)
# print(set3)
#
# set1={1,2,3,4,5,6}
# set2=[4,5,6,7,8,9]
# set3=set1.union(set2)
# print(set3)


##add
# set1={1,2,3,4,5}
# set1.add(6)
# print(set1)

##update
# sub_name1={"phy","che","math"}
# sub_name2={"bio","eng"}
# # sub_name1.update(sub_name2)
# # print(sub_name1)
# # print(sub_name2)
# sub_name2.update(sub_name1)
# print(sub_name1)
# print(sub_name2)

##union
# set1={1,2,3,4,5,3}
# set2={4,5,6,6,7,8}
# set3=set1.union(set2)
# print(set1)
# print(set2)
# print(set3)

##delete
##1.remove
# set1={1,2,3,4,5}
# set1.remove(3)
# print(set1)

##discard
# names1={"Pooja","Ankit","Saurav","Pankaj"}
# # names1.discard("Ankit")
# # print(names1)
# names1.discard("saurav")
# print(names1)

##pop

# names1={"Pooja","Ankit","Saurav","Pankaj"}
# names1.pop()
# print(names1)

##clear()
# set1={"Pooja","Ankit","Sawant",5,4,7,8}
# set1.clear()
# print(set1)

##delete()
##use to delete variable
# names1={"Pooja","Ankit","Saurav","Pankaj"}
# del names1()
# print(names1)

##Intersection()
# set1={10,20,40,60,80}
# set2={30,40,50,60,70,80}
# # set1.intersection(set2)
# # print(set1)
# set2.intersection(set1)
# print(set2)
# set3=set2.intersection(set1)
# print(set3)

# fru_names1 = {'mango','apple','banana','berry'}
# fru_names2 = {'mango','grape'}
#
# print(fru_names1.intersection(fru_names2))


##intersection_update
# names1 = {"Pooja","Ankit","Saurav","Pankaj"}
# names2 = {"Saurav","Pankaj","Raju","Sanket"}
# # names1.intersection_update(names2)
# # print(names1)
# # print(names2)
#
# names2.intersection_update(names1)
# print(names1)
# print(names2)

##difference
# names1 = {"Pooja","Ankit","Saurav","Pankaj"}
# names2 = {"Saurav","Pankaj","Raju","Sanket"}
# print(names1.difference(names2))
# print(names2.difference(names1))

# names1 = {"Pooja","Ankit","Saurav","Pankaj"}
# names2 = {"Saurav","Pankaj","Raju","Sanket"}
#
# set3 = names1.difference(names2)
#
# print(names1)
# print(names2)
# print(set3)

##

# set1={10,20,40,60,80}
# set2={30,40,50,60,70,80}
# set3=set1.intersection(set2)
# print(set1)
# print(set2)
# print(set3)

##symmetric difference

# names1 = {"Pooja","Ankit","Saurav","Pankaj"}
# names2 = {"Saurav","Pankaj","Raju","Sanket"}
#
# set3 = names1.symmetric_difference(names2)
#
# print(names1)
# print(names2)
# print(set3)

##symmetric diif update
# names1 = {"Pooja","Ankit","Saurav","Pankaj"}
# names2 = {"Saurav","Pankaj","Raju","Sanket"}
#
# set3 = names2.symmetric_difference_update(names1)
#
# print(names1)
# print(names2)
# print(set3)

##is subset
# set1 = {1,2,3,4,5,6}
# set2 = {4,3,5}
#
# print(set2.issubset(set1))

# set1 = {1,2,3,4,5,6}
# set2 = {4,3,5}
#
# print(set1.issubset(set2))


##issuperset
# set1 = {1,2,3,4,5}
# set2 = {3,4,5}
#
# print(set1.issuperset(set2))

# set1 = {1,2,3,4,5}
# set2 = {3,4,5}
#
# print(set2.issuperset(set1))


##is disjoint
# set1 = {1,2,3}
# set2 = {4,5,6}
#
# print(set1.isdisjoint(set2))

# set1 = {1,2,3}
# set2 = {3,5,6}
#
# print(set1.isdisjoint(set2))











