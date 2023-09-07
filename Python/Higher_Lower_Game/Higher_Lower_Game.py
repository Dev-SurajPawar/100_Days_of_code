import random
from Game_data_Higher_Lower import data


def format_data(compare):
    account_name = compare["name"]
    account_descr = compare["description"]
    account_country = compare["country"]
    return f"{account_name}, a {account_descr}, form {account_country}"


def check_ans(user_guess, follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return user_guess == "A"
    else:
        return user_guess == "B"


score = 0
game_should_continue = True
compare_B = random.choice(data)

while game_should_continue:

    compare_A = compare_B
    compare_B = random.choice(data)

    if compare_A == compare_B:
        compare_B = random.choice(data)

    print(f"Compare A: {format_data(compare_A)}.")
    print("Vs")
    print(f"Against B: {format_data(compare_B)}.")

    guess = input("Who has more follower? Type 'A' or 'B': ").upper()

    follower_count_A = compare_A["follower_count"]
    follower_count_B = compare_B["follower_count"]
    is_Correct = check_ans(guess, follower_count_A, follower_count_B)

    if is_Correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {score}")
