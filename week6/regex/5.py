import re 

s = input()
pattern = r'a.*b$'
some = re.search(pattern, s)
if some:
    print("Yes")
else:
    print("No")
