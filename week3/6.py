def jimin(a):
    sentence = a.split()
    rsentence = ' '.join(reversed(sentence)) 
    return rsentence

c = input()
b = jimin(c)
print(b)
