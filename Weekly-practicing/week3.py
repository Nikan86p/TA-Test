import random

n = 1
m = 10
x = random.randint(n, m)

while True:
    user_guess = int(input(f"What is your guess? betwwen({n},{m}) : "))
    if user_guess != x:
        if user_guess > x:
            m = user_guess
            print("Too High!!")
        elif user_guess < x:
            n = user_guess
            print("Too Low!!!")

    if x == user_guess:
        print("Your guess is correct!!!")
        break
