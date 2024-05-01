# st.format() = optional method that gives users
#               more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
print("the {} jumped over the {}".format(animal,item))

# ---------- positional argument -------------
print("the {1} jumped over the {0}".format(animal,item)) 

# ---------- keyword argument -------------
print("the {animal} jumped over the {item}".format(animal="lion",item="bad")) 


# ---------- third method -------------
text = "the {} juped over the {}"
print(text.format(item, animal))
