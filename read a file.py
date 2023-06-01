try:
    with open("test.txt") as file:
        content = file.read()
        if 'yoo' in content:
            print("work")
except FileNotFoundError:
    print("This file is not found.")

