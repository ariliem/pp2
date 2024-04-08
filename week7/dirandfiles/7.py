with open("file.txt", "w") as s:
    s.write("This is first file")

with open("file.txt", "r") as s:
    print(s.readline())

with open("file2.txt", "w") as s2:
    with open("file.txt", "r") as s:
        for line in s:
            s2.write(line)

with open("file2.txt", "r") as s2:
    print(s2.readline())
