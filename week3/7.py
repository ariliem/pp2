n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
def has_33(a):
    n = len(a)
    for i in range(n-1):
        if a[i] == 3  and a[i+1] == 3:
            return True 
        else:
            return False
    
print(has_33(a))
