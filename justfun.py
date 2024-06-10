def jetur():
    print("Sum of Two Numbers")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

def kron():
    text = input("Enter the text to print five times: ")
    for _ in range(5):
        print(text)


while True:
    user_choice = input("What do you want to do? [sum, 5times, exit]: ").strip().lower()
    if user_choice == 'sum':
        jetur()
    elif user_choice == '5times':
        kron()
    elif user_choice == 'exit':
        break
    else:
        print("Invalid option. Please choose 'sum', '5times', or 'exit'.")
