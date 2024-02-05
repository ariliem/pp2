from movies import movies

def category(category):
    for i in movies:
        if i["category"] == category:
            print(i["name"])

category1 = input()
category(category1)