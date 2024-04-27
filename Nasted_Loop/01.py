# Nasted Loop
'''
This "inner loop" will finish akk if it's iteration befire
finishing one iteration of the "Outer Loop"
'''

rows = int(input("How many Rows ? :"))
colums = int(input("How many columns ? :"))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for l in range(colums):
        print(symbol, end="")
    print()

