import sys
import math
from abc import ABCMeta, abstractmethod
sys.stdout.reconfigure(encoding="utf-8")

class Employee(metaclass = ABCMeta):
    def __init__(self , name : str):
        self.name = name
    
    @abstractmethod # このアノテーションで抽象クラスになる
    def getBonus(self , amount : int) -> int:
        pass
    
class JuniorEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)
    
    def getBonus(self, base : int) -> int:
        return math.floor(base * 1.1)
    
class MiddleEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)
    
    def getBonus(self, base : int) -> int:
        return math.floor(base * 1.5)
    
class SeniorEmployee(Employee):
    def __init__(self, name):
        super().__init__(name)
    
    def getBonus(self, base : int) -> int:
        return math.floor(base * 2.0)
    
if __name__ == "__main__":
    emp1 = JuniorEmployee("Yamada")
    emp2 = MiddleEmployee("Suzuki")
    emp3 = SeniorEmployee("Kudo")
    
    base = 100
    print("-------")
    print(emp1.getBonus(base))
    print(emp2.getBonus(base))
    print(emp3.getBonus(base))