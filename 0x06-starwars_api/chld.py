import random

def generate_problem():
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    return x, y, x + y

def validate_input(user_input):
    return user_input.isdigit()

def solve_problem(x, y, answer):
    tries = 0
    while tries < 3:
        user_input = input(f"What is {x} + {y}? ")
        if validate_input(user_input):
            user_answer = int(user_input)
            if user_answer == answer:
                return True
            else:
                print("EEE")
        else:
            print("EEE")
        tries += 1

    print(f"The correct answer is {answer}.")
    return False

def main():
    level = input("Choose a level (1, 2, or 3): ")
    while level not in ['1', '2', '3']:
        level = input("Invalid level. Choose a level (1, 2, or 3): ")

    level = int(level)
    score = 0

    for _ in range(10):
        x, y, answer = generate_problem()
        if solve_problem(x, y, answer):
            score += 1

    print(f"Your score is: {score} out of 10.")

if __name__ == '__main__':
    main()