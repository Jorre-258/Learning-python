import os

source = ("test.txt")
destination = ("C:\\Users\\JoranDelcroix\\Documents\\python\\test1.txt")

try:
    if os.path.exists(destination):
        print("There is already a file.")
    else:
        os.replace(source, destination)
        print(source + " has been moved")

except FileNotFoundError:
    print(source + " was not found:(")
