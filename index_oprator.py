# index operator [] = gives access to a sequence's element (str,list,tuples)

# j e t u r   g a v l i !
# 0 1 2 3 4 5 6 7 8 9 10 11

name = "jetur gavli!"

'''
if(name[0].islower()):
    name = name.capitalize()

print(name)
'''

first_name = name[0:5].upper()
last_name = name[6:].lower()
last_character = name[-1]

print(first_name)
print(last_name)

print(last_character)
