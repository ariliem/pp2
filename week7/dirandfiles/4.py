with open ("some",'w') as s:
    s.write("""There we have
    two lines""")
with open("some", 'r') as s2:
    lines = len(s2.readlines())
    print(lines)
