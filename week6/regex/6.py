import re

s = input()
pattern = r'[,\s.]'

a = re.sub(pattern, ":" ,  s)

print(a)