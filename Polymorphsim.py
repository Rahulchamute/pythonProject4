import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area_circle=math.pi*self.radius**2
        print("area of circle=",area_circle)

class square():
    def __init__(self,side):
        self.side=side
    def area(self):
        area_square=self.square**2
        print("area of square=",area_square)
class rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area_rect=b*h
        print("area of Rectangle=",area_rect)

c1=circle(5)
c1.area()
# def exe_func():
#     c1 = circle(5)
#     s1 = square(6)
#     r1 = rectangle(5, 6)
#     for obj in [c1, s1, r1]:
#         obj.area()
# exe_func()