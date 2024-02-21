import re 

a = input()
pattern = r'ab{2,3}'

s = re.search(pattern, a)

if s:
    print("Yes")
else:
    print("No")