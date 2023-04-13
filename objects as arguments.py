class Car:
    color = None

class Motorcycle:
    color = None

def chance_color(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

chance_color(car_1,"red")
chance_color(car_2,"white")
chance_color(car_3,"blue")

chance_color(bike_1, "black")
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)