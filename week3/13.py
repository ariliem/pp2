import random
num = random.randint(1,20)

def guess(n):
    x = int(input())
    if x<num:
        print("Your guess is too low.")
        print("Take a guess.")
        guess(n+1)
    elif x>num:
        print("Your guess is too high.")
        print("Take a guess.")
        guess(n+1)
    elif x==num:
        print ("Good job, "+ name + "!",end=' ')
        print("You guessed my number in " + str(n) + " guesses!")

print("Hello! What is your name?")
name = input()
print("Well, "+name+", I am thinking of a number between 1 and 20.")
print("Take a guess.")
  
guess(1)