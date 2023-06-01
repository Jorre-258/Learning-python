double = lambda x: x * 2
print(double(5))

multiply = lambda x, y: x * y
print(multiply(4,5))

add = lambda x, y, z: x + y + z
print(add(5, 8, 9))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Joran", "Delcroix"))

check_age = lambda age: True if age >= 18 else False
print(check_age(19))