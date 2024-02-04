def solve(h,l):
    rabbits = int((l - 2*h) / 2)
    chickens = int(h - rabbits)
    print(rabbits, " ", chickens)

h = 34
l = 94

solve(h,l)