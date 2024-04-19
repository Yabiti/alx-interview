import sys
import random
i = 100
random.randint(1,10)
n = int(input("level: "))
while i > 1:
    if i == n:
        sys.exit("just right")
    elif i < n:
        print("Too small")
        n = int(input("Guess: "))
    else:
        print("Too large")
        n = int(input("Guess: "))