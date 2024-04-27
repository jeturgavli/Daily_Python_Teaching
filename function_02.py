# function = a block of code which is executed only when it is called.

def get_info():
    first_name = input("What is your Name? : ")
    last_name = input("What is your Surname? : ")
    age = int(input("What is your Age ? : "))
    return first_name, last_name, age

def Hello(first_name, last_name, age):
    print("Hello "+first_name+" "+last_name )
    print("Your are "+str(age)+" year old")
    print("Have a Good Day Sir!")


first_name, last_name, age = get_info()
Hello(first_name, last_name, age)
