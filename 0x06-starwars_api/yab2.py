import sys
import random

i = random.randint(1,100)
i = 1
n = int(input("level: "))
n = int(input("guess: "))
while i < 100:
    if n < 0:
        n = int(input("level: "))
    if n < i:
        sys.exit("Too small")
    if i == n:
        sys.exit("just right!")
    if n > i:
        sys.exit("Too large")
    else:
        print(input("Level: "))
