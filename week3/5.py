def jimin(a):
    
    from itertools import permutations
    p = permutations(a)
    for j in p:
        print(j)
a = input()
jimin(a)