import re

s = input()
pattern = r'[A-Z]'

x = re.split(pattern, s)
print(x)