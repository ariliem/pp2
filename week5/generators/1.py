def jimin(n):
    for i in range(1, n+1):
        yield i**2

a = int(input())
sq = jimin(a)

for sqq in sq:
    print(sqq)