import random

i = 100
n = int(input("Guess: "))
while i < 1:
    if i < 1:
        n = int(input("Guess: "))
    elif i == n:
        print("just right!")
    elif i > n:
        print("Too large")
    else:
        print("Too small")

i = random.randint(1,100)
print(i)