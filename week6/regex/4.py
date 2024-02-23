import re

s = input()
pattern = r'[A-Z][a-z]+'

some = re.findall(pattern, s)


if some:
    print("Yes")

else:
    print("No")






