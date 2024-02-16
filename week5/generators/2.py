def even(n):
    for i in range(0, n+1):
        if i%2==0:
            yield i

a = int(input())
ev = even(a)
print(*ev, sep =", ")