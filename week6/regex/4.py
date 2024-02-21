# import re

# s = input()
# pattern = r'[A-Z][a-z]+'

# some = re.findall(pattern, s)


# if some:
#     print("Yes")

# else:
#     print("No")


import re

s = input()
pattern = r"[A-Z][a-z]+"  # Regex for upper case followed by one or more lower case
matches = re.findall(pattern, s)
if matches:
    print("Yes")

else:
    print("No")




