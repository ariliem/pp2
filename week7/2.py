s = input()
countUpper = 0
countSlower = 0
for x in s:
    if x.isupper():
        countUpper += 1
    else:
        countSlower += 1
print("Amount of upper letters: " ,  countUpper)
print("Amount of slower letters: " ,  countSlower)
