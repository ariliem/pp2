import re

s = input()
  
x = re.sub(r'(?:^|_)([a-z])', lambda match: match.group(1).upper(), s)
print(x)
