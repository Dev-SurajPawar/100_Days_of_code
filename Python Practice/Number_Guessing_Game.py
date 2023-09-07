import random

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_ans(guess, ans, turns):
    if guess > ans:
        print("To High.")
        return turns - 1
    elif guess < ans:
        print("To Low.")
        return turns - 1
    else:
        print("You win")


def game_Level():
    level = input("Chose the difficulty. Type 'Easy' or 'Hard': ").upper()
    if level == "HARD":
        return HARD_LEVEL_TURN
    elif level == "EASY":
        return EASY_LEVEL_TURN
    else:
        print("Select the correct game level")


def game():
    print("Welcome to the Number Guessing Game!!")
    print("I'm thingking of a number between 1 and 100")
    ans = random.randint(1, 100)
    turns = game_Level()
    guess = 0
    while guess != ans:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        turns = check_ans(guess, ans, turns)
        if turns == 0:
            print(f"You run out of guesses, you lose Number is: {ans}")
            return
        elif guess != ans:
            print("Guess again.")


game()