import sys
import random

i = random.randint(1,100)
i = 1
n = int(input("level: "))
while i < 100:
    if n < 0:
        n = int(input("level: "))
    if i < n:
        sys.argv("Too small")
    if i == n:
        sys.argv("just right!")