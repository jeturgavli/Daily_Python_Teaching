# prevents a user from creating an object of that class
#  + compels a user to override abstact methods in a child class

# abstract class = a class which contains one or more abstact methods.
# abstract method = a method that has a declaration but does not have an implementaion.

from abc import ABC, abstractmethod

class gaadi(ABC):
    @abstractmethod
    def go (self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(gaadi):
    def go(self):
        print("oh.. Bhai gadi chal rahi he")

    def stop(self):
        print("oh.. bhai gadi ka petrol khtam ho gya ..")

class Motorcycle(gaadi):
    def go(self):
        print("oh.. ride the motorcycle")
    def stop(self):
        print("oh.. bike ka engine gyaa")

# vehicle = gaadi()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()