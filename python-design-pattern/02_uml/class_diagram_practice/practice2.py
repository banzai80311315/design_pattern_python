from abc import ABCMeta, abstractmethod

#インターフェイス（抽象クラス）
class Shape(metaclass = ABCMeta):
    @abstractmethod # このアノテーションで抽象クラスになる
    def calc_area(self) -> int:
        pass
    
#引数に抽象クラスを渡せば継承される
class Rectangle(Shape):
    def __init__(self , width: int , height: int):
        self.__width = width
        self.__height = height
    
    def calc_area(self) -> int:
        return self.__width * self.__height
    

class Square(Shape):
    def __init__(self , length: int):
        self.__length = length
        
    def calc_area(self):
        return self.__length ** 2
    
class Client:
    def __init__(self , shape: Shape):
        self.__shape = shape
        
    def getShape(self):
        return self.__shape