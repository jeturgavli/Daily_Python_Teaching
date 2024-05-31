# its very hard and bad process to work with class

class Rabbit():
    alive = True
    def eat(self):
        print("This animal is eating")
    def slumbr(self):
        print("This animal is sleeping")
class Fish():
    alive = True
    def eat(self):
        print("This animal is eating")
    def slumbr(self):
        print("This animal is sleeping")
class Hawk():
    alive = True
    def eat(self):
        print("This animal is eating")
    def slumbr(self):
        print("This animal is sleeping")

rabbit = Rabbit()
fish = Fish()
hwak= Hawk()

print(rabbit.alive)
fish.eat()
hwak.slumbr()