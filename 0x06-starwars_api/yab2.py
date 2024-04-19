import sys
import random
i = 1
random.randint(1,10)
n = int(input("level: "))
n = int(input("Guess: "))
while i != 100:
    if i == n:
        sys.exit("just right")
    elif i < n:
        print("Too small")
        n = int(input("Guess: "))
    else:
        print("Too large")
        n = int(input("Guess: "))
