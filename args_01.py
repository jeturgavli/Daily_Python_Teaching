#  *args = parameter that will pack all  arguments into a tuple
#          useful so that a function can acceot a varying amount of arguments

"""
def add(num1,num2):
    sum = num1 + num2
    return sum

print(add(1,2))
"""
"""
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,5,6))
"""
'''
def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

'''