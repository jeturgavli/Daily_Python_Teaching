# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car :

    def turnon(self):
        print("you start the engine")
        return self
    
    def drive(self):
        print("you drive the car")
        return self
    
    def brake(self):
        print("You stop on the brakes")
        return self
    
    def turnoff(self):
        print("You turn off the engine")
        return self

car = Car()

car.turnon().brake().turnon().drive().turnoff

