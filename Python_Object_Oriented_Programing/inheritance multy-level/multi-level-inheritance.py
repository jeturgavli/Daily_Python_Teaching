# Multi level inheritance = when a derived (child) class inherits another dervid (child) class 

class Organism: # Grant Perent
    alive = True

class Animal(Organism): # Parent
    def eat(self):
        print("This animal is eating")

class Dog(Animal): # child
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)    # inherited from the Organism Class
dog.eat()           # inherited from the Animal class
dog.bark()          # defined in Dog class


