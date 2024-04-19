import random

i = 100
n = input("Guess: ")
while True:
    if i < 1:
        n = input("Guess: ")
    elif i == n:
        print("just right!")
        break
    elif i > n:
        print("Too large")
        n = input("Guess: ")
    else:
        print("Too small")
        n = input("Guess: ")

i = random.randint(1,100)