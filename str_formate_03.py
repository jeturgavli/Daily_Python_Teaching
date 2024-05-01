# st.format() = optional method that gives users
#               more control when displaying output

print("-----First Veriason -----")
number1 = 3.14159
print(f"Number 1 orignal Value {number1}")
print("The number pi is {:.2f}".format(number1))
print("The number pi is {:.3f}".format(number1))

print("\n-----Secound Veriason Coma (,)-----")
number2 = 1000
print(f"Number 2 orignal Value {number2}")
print("The number pi is {:,}".format(number2))

print("\n-----Therd Veriason bianary-----")
number3 = 1000
print(f"Number 3 orignal Value {number3}")
print("The number pi is {:b}".format(number3))

print("\n-----Forth Veriason Octal -----")
number4 = 1000
print(f"Number 4 orignal Value {number4}")
print("The number pi is {:o}".format(number4))

print("\n-----Fifth Veriason Heximal small x -----")
number5 = 1000
print(f"Number 5 orignal Value {number5}")
print("The number pi is {:x}".format(number5))

print("\n-----Sixth Veriason Heximal capital X -----")
number6 = 1000
print(f"Number 6 orignal Value {number6}")
print("The number pi is {:X}".format(number6))

print("\n-----Sevanth Veriason Sintafic knocation small e -----")
number7 = 1000
print(f"Number 7 orignal Value {number7}")
print("The number pi is {:e}".format(number7))

print("\n-----Eighth Veriason Sintafic knocation capital E -----")
number8 = 1000
print(f"Number 8 orignal Value {number8}")
print("The number pi is {:E}".format(number8))