n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
def spy_game(a):

    has0 = False
    has00 = False

    for b in a:
        if b == 0 and not has0:
            has0 = True
        elif b == 0 and has0 and not has00:
            has00 = True
        elif b == 7 and has0 and has00:
            return True

    return False

print(spy_game(a))
