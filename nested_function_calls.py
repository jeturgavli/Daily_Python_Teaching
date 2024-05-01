# Nested function calls = function calls inside other function calls
#                         innermost function calls are resolved fist
#                         returned value is used as agrument for the next outer function

# num = input("Enter a whole positive number : ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# --- this is one line code
print(round(abs(float(input("Enter a whole positive number : ")))))
