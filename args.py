
def add(*args):
    sum = 0
    args = list(args)
    args[2] = 0    # error   args cannot chance
    for i in args:
        sum += i
    return sum

print(add(1,2,4,5,53,63,967))