# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keword arguments

# --------- this is error mid not working ----
'''
def hello(fist,last):
    print("Hello "+ fist + " " + last)

hello(fist="Jetur",mid = "Rajeshbhai",last="gavli")
'''

# ---------- this is with kwarge mid value not working in output but still program is running
'''
def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])

hello(first="Jetur", mid="Rajesh bhai", last="Gavli")
'''

# -----this is final program doesnt min how many key in this program its show all
''''''
def hello(**land):
    print("Hello", end=" ")
    for key,value in land.items():
        print(value, end=" ")

hello(title="Mr.", first="Jetur", mid="Rajeshbhai", last="Gavli")