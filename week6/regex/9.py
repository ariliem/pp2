import re
s = input()
a = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
print(a)


