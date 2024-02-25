import re

s = input()

x = re.sub(r'(?<!^)(?=[A-Z])', "_", s).lower()

print(x)






