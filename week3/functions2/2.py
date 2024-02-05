from movies import movies

import random

def jimin():
    for i in range(len(movies)):
        if movies[i]["imdb"] >= 5.5:
            print(movies[i]["name"])

jimin()