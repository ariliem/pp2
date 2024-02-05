n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
def histogram(numbers):
    for num in numbers:
        print('*' * num)

histogram(a)