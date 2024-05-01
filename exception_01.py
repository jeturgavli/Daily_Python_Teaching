# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denumerator = int(input("Enter a number to divide by: "))
    result = numerator / denumerator
except ZeroDivisionError as e:
    print(e)
    print("Are u idiot ? You can't divide by Zero! ")
except ValueError as e:
    print(e)
    print("Enter only number Plzz .. :'(")
except Exception as e:
    print(e)
    print("Something went wrong !!! :(")
else:
    print(result)