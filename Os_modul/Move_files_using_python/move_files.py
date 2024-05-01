import os

source = "Move2.txt"
destination = r"C:\Users\JETRock\Desktop\Teaching_Python\Os_modul\Move_files_using_python\example_folder1\Move2.txt"
destination = destination.replace('\\','\\\\')

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " Was move")

except FileNotFoundError:
    print(source + " was not found")
