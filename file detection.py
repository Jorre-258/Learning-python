import os
path = "C:\\Users\\JoranDelcroix\\Documents\\python" # \\test.txt"
if os.path.exists(path):
    print("This location exists.")
    if os.path.isfile(path):
        print("That file exists.")
    elif os.path.isdir(path):
        print("That is a directory.")
else:
    print("This location doesn't exists.")
