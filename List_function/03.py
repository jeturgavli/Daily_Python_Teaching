

'''
tuple = collection which is ordered and unchangeable
        used to group togather related data 
'''

student = ("Jetur",21,"male")

print(student.count("Jetur"))
print(student.index("male"))

for x in student:
    print(x)

if "male" in student:
    print("i am here!")
