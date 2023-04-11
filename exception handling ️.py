try:
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a number to divide by:"))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! You idiot!")
except ValueError as e:
    print(e)
    print("Enter a number!")
except Exception:
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")


