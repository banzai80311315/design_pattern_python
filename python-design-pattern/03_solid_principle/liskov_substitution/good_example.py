import sys
import math
from abc import ABCMeta, abstractmethod
sys.stdout.reconfigure(encoding="utf-8")

class Shape(metaclass = ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod # このアノテーションで抽象クラスになる
    def getArea(self) -> int:
        pass
    
class Rectangle(Shape):
    def __init__(self):
        self.__width = 0
        self.__height = 0
        
    @property
    def width(self) -> int:
        return self.__width
    
    @width.setter
    def width(self , width : int):
        self.__width = width
        
    @property
    def height(self) -> int:
        return self.__height
    
    @height.setter
    def height(self , height : int):
        self.__height = height
        
    def getArea(self) -> int:
        return self.width * self.height
    
class Square(Shape):
    def __init__(self):
        self.__length = 0
        
    @property
    def length(self) -> int:
        return self.__length
    
    @length.setter
    def length(self , length : int):
        self.__length = length
        
    def getArea(self) -> int:
        return self.length ** 2
    
def f(shape : Shape) -> int:
    print(shape.getArea())
    
    # ポリモーフィズム：ひとつのコードで複数のオブジェクトに切り替えができること
    
if __name__ == "__main__":
    r1 = Rectangle()
    r2 = Square()

    r1.width = 3
    r1.height = 4
    
    r2.length = 4
    
    f(r1)
    f(r2)