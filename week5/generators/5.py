def tozero(n):
    while n != -1:
        yield n
        n = n-1


n = int(input())
res = tozero(n)
for i in res:
    print(i)