# return statement = functions send python values/objects back to the caller.
#                    These values/objects are known as the function's return value

print(" ---- Multiply Program Help of Return Statement ---")

def multiply(number1,number2):
    return number1 * number2

land = int(input("Enter Your First Number : "))
bhosdo = int(input("Enter Your Secound Number : "))

x = multiply(land,bhosdo)
print(x)
