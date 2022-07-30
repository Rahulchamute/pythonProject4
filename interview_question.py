## find maximum no of list
# def my_max(li):
#     max=li[0]
#     for i in li:
#         if (i>max):
#             max=i
#     return max
# li1=[10,20,30,40,50]
# print("Maximum element=",my_max(li1))

# li1=[10,30,70,50,60]
# #print(max(li1))
# li1.sort()
# print(li1[-1])

#### find minimum no of list
# def my_min(li):
#     min=li[0]
#     for i in li:
#         if (i<min):
#             min=i
#     return min
# li1=[5,6,8,1,2]
# print("minimum element=",my_min(li1))

# li1=[5,6,8,1,2]
# print(min(li1))

# li1=[5,6,8,1,2]
# li1.sort()
# print(li1[0])


##square value using lambda
# a=range(1,11)
# res=list(map(lambda a:a*a,a))
# print(res)

##Even odd
# a=range(1,11)
# res=list(filter(lambda a:a%2==0,a))
# print(res)
#
# a=range(1,11)
# res=list(filter(lambda a:a%2!=0,a))
# print(res)

## calculate days
# def test_gen(index):
#     weekdays=['sun','mon','Tue','wed','thu','fri','sat']
#     yield weekdays[index]
#     yield weekdays[index+1]
# day=test_gen(0)
# print(next(day),next(day))

##
# import numpy as np
# a=np.array([1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
# print(a)
# print(a.pop())
# print(a.pop(3))
# a.remove(1.1)
# print(a)



##dict
# a={1:6,2:4,3:1,4:5}
# print(sorted(a.values()))



