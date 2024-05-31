class animal:
    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(animal):
    def run(self):
        print("This rabbit is running")
class Fish(animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hwak = Hawk()

print("First Result \n")
print(rabbit.alive)
fish.eat()
hwak.sleep()

print("\n")

print("Secound Result \n")
rabbit.run()
fish.swim()
hwak.fly()