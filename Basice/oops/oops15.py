#abstract based class

from abc import ABCMeta,abstractmethod

class  shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle:
    type ="Rectangle"
    side = 4
    def __init__(self) -> None:
        self.length=6
        self.breadth=7

    def printarea(self):
        return self.length * self.breadth


rect1=Rectangle()
print(rect1.printarea())
