from movies import movies

def average():
    total = 0
    for i in movies:
        total = total + i["imdb"]
    average = total / len(movies)

    print(round(average, 1))

average()