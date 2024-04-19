import random

i = 1
n = int(input("Guess: "))
while True:
    if i < 100:
        random.randint(1,100)
    elif i == n:
        print("just right")
    elif i < n:
        print("Too small")
    else:
        print("Too large")
    
