# Scop =  The region that a variable is recognized 
#         A Variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

name = "Jetur" # Global scope (available inside & outside functions)

def display_name():
    name = "Gavli" # loacl scope (available only inside this function)
    print(name)

display_name()
print(name)

# L = Local
# E = Enclosing
# G = Global
# B = Built-in
