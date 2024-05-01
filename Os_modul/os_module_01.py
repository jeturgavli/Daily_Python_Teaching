import os

# ------------ Basic File Ditection Program ----------

# path = "c:\\Users\\JETRock\\Desktop\\Teaching_Python\\Os_modul\\test.txt"
path = "c:\\Users\\JETRock\\Desktop\\Teaching_Python\\Os_modul\\Test"

if os.path.exists(path):
    print("Yes this location exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("That is a Direcotry!")
else:
    print("No this location not exists")
