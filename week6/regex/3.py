import re

s = input()
pattern = r'[a-z]_[a-z]'

some = re.search(pattern, s)

if some:
    print("Yes")
else:
    print("No")