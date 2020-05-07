import os
path=input("Enter your path : ")

if os.path.exists(path):
    print(f"Given Path is {path} is valid")
    if os.path.isfile(path):
        print(f" This is FILE {path}")
    else:
        print(f"this is DIR {path}")
else:
    print(f"Not a valid path")
