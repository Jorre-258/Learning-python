import random
x = random.randint(1,6)
y = random.random()

print()

myList = ["Rock","Paper","Scissors"]
z = random.choice(myList)
print()

cards = [1,2,3,4,5,6,7,8,9,"Jack","Queen","King","Ace"]
random.shuffle(cards)
print(cards)


