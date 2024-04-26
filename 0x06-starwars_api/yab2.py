import sys 
import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

n = random.randint(1, level)
while True:
    guess = int(input("guess: "))
    if guess > 0:
        if guess == n:
            print("just right")
        elif guess < n:
            print("Too small")
        elif guess > n:
            print("Too large")
            break
