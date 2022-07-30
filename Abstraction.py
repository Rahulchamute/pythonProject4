

from abc import ABC,abstractmethod

# class ProjectBlueprint(ABC):
#     @abstractmethod
#     def Resigstration(self):
#         pass
#     @abstractmethod
#     def Login(self):
#         pass
#     @abstractmethod
#     def Forget_password(self):
#         pass
#
#     def Process_document(self):
#         pass
#
# class ProjectAPI(ProjectBlueprint):
#     def Resigstration(self):
#         print("This is Resistration API")
#
#     def Login(self):
#         print("This is login API")
#
#     def Forget_password(self):
#         print("This is forget password API")
#
#     def Process_document(self):
#         print("This is process document API")
#
# obj1=ProjectAPI()
# obj1.Login()
# obj1.Forget_password()


class Shape(ABC):
    @abstractmethod
    def volume(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Cube(Shape):
    def __init__(self, side):
        print("Cube Class __init__ Method")
        self.side = side
    def volume(self):
        vol = self.side ** 3
        print(f"The Volume of Cube = {vol}")
    def area(self):
        ar = self.side * self.side * 6
        print(f"The Area of the Cube = {ar}")
    def print_side(self):
        print(f"The side of Cube = {self.side}")
c1 = Cube(5)
c1.volume()
c1.area()
c1.print_side()