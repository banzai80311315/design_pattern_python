from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        
class Movable(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Flyable(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class Airplane(Vehicle , Movable , Flyable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self):
        print("airplane start!")

    def stop(self):
        print("airplane stop!")

    def fly(self):
        print("airplane fly!")


class Car(Vehicle , Movable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self):
        print("car start!")

    def stop(self):
        print("car stop!")


if __name__ == "__main__":
    v1: Vehicle = Airplane("AirBus", "white")
    v2: Vehicle = Car("Prius", "black")

    v1.fly()
    v1.start()
    v1.stop()
    
    v2.start()
    v2.stop()
