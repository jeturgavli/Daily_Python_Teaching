
try:
    with open('test.txt') as file:
          print(file.read())
except FileNotFoundError:
     print("that file is not found")



