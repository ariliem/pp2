import re 

a = input()
pattern = r'ab*'

s = re.search(pattern, a)

if s:
    print("Yes")
else:
    print("No")