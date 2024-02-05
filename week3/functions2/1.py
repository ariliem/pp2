import random

from movies import movies

def jimin():
    a = random.choice(movies)
    if a["imbd"]>=5.5:
        return True
    else:
        return False

print(jimin())