from car import Car

car1 = Car("Chevy","Corvette", 2021, "Red")
car2 = Car("Ford","Mustang", 2022, "Black")

car1.wheel = 2

Car.wheel = 6 # changed car wheel class value into program main file 
print(car1.wheel)
print(car2.wheel)
