def thfo(n):
    for i in range(n+1):
        if i%3 == 0 and i%4 == 0:
            yield i

a = int(input())
res = list(thfo(a))
print(res)



