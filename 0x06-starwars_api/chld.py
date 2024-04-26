import random

def generate_integer(level):
    x = random.randint(1,10)
    y = random.randint(1,10)
    return x,y , x + y

def user_input():
    return user_input()

def answer(correct_answer):
    i = 0
    while i < 3:
        if user_input == correct_answer:
            return True
        else:
            print("EEE")
        i += 1
